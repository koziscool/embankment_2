

import time

def e10():

    end_range = 2 * 10 ** 6
    def primes_and_totients( num ):
        primes = []
        totients = [1 for i in xrange(num + 1)]
        for i in xrange(2, num + 1):
            if totients[i] == 1:
                primes.append(i)
                for j in xrange(i, num + 1, i):
                    totients[j] *= i - 1
                    k = j / i
                    while k % i == 0:
                        totients[j] *= i
                        k /= i

        return primes, totients

    return sum( primes_and_totients( end_range )[0] )

if __name__ == "__main__":
    start = time.time()
    # print
    print
    print "Euler 10 solution is:",  e10()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


