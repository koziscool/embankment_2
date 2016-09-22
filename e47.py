import time
import operator

def e47():
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

    primes_and_totients( begin_cursor, end_cursor )

    test_cursor = 2

    while True:
        if test_cursor + 3 > end_cursor:
            begin_cursor, end_cursor = end_cursor + 1, 2* end_cursor
            primes_and_totients( begin_cursor, end_cursor )    

        if ( len( prime_divisors[test_cursor] ) == 4 and len( prime_divisors[test_cursor+1] ) == 4
                and len( prime_divisors[test_cursor+2] ) == 4 
                and len( prime_divisors[test_cursor+3] ) == 4 ):

            # print prime_divisors[test_cursor], prime_divisors[test_cursor+1], \
                    # prime_divisors[test_cursor+2], prime_divisors[test_cursor+3]
            break
        test_cursor += 1

    return test_cursor

if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 47 solution is:",  e47()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


