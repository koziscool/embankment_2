import time
import operator

def e12():
    prime_divisors = { 1: [] }
    begin_cursor, end_cursor = 2, 200
    primes = []
    totients = [1, 1]

    def primes_and_totients( begin_cursor, end_cursor ):

        new_totients = [1 for i in xrange(end_cursor - begin_cursor + 1)]
        totients.extend( new_totients )

        for p in primes:
            begin_range = ((begin_cursor / p) + 1) *p
            if begin_cursor % p == 0:
                begin_range = begin_cursor
            for j in xrange(begin_range, end_cursor + 1, p):
                if j in prime_divisors:
                    prime_divisors[j].append( p )
                else:
                    prime_divisors[j] = [p]

                totients[j] *= p - 1
                k = j / p
                while k % p == 0:
                    totients[j] *= p
                    k /= p

        for i in xrange( begin_cursor, end_cursor + 1 ):
            if totients[i] == 1:
                primes.append(i)
                for j in xrange(i, end_cursor + 1, i):
                    if j in prime_divisors:
                        prime_divisors[j].append( i )
                    else:
                        prime_divisors[j] = [i]
                    totients[j] *= i - 1
                    k = j / i
                    while k % i == 0:
                        totients[j] *= i
                        k /= i

    def get_factors( n ):
        prime_product = reduce( operator.mul, prime_divisors[n], 1)
        reduce_quotient = n / prime_product
        factors_dict = { p:1 for p in prime_divisors[n] }
        while reduce_quotient != 1:
            prime_product = reduce( operator.mul, prime_divisors[reduce_quotient], 1)
            for p in prime_divisors[reduce_quotient]:
                factors_dict[p] += 1
            reduce_quotient /= prime_product

        return factors_dict

    primes_and_totients( begin_cursor, end_cursor )

    triangle_cursor = 1
    while True:
        triangle = triangle_cursor * (triangle_cursor + 1) / 2

        if triangle_cursor + 1 > end_cursor:
            begin_cursor, end_cursor = end_cursor + 1, 2* end_cursor
            primes_and_totients( begin_cursor, end_cursor )

        factors_1 = get_factors( triangle_cursor )
        factors_2 = get_factors( triangle_cursor + 1)
        combined_factors = dict(factors_1, **factors_2)
        combined_factors[2] -=1
        num_factors = reduce( operator.mul, map( lambda n: n+1, combined_factors.values() ), 1)

        if num_factors > 500:
            break

        triangle_cursor += 1

    return triangle


if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 12 solution is:",  e12()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


