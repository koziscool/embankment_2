import time

def e5():
    primes = [ 2, 3, 5, 7, 11, 13, 17, 19 ]
    lcm_factors = {}

    for i in xrange( 1, 21 ):
        quotient = i
        for p in primes:
            divisor_count = 0
            while quotient % p == 0:
                divisor_count += 1
                if p not in lcm_factors:
                    lcm_factors[p] = 1
                elif divisor_count > lcm_factors[p]:
                    lcm_factors[p] = divisor_count

                quotient /= p

    lcm = 1
    for factor, exponent in lcm_factors.items():
        lcm *= pow(factor, exponent)


    return lcm



if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 5 solution is:",  e5()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),
