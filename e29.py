import time

def e29():
    power_set = set()
    for base in xrange(2, 101):
        for exp in xrange(2, 101):
            power_set.add( pow(base, exp) )
    return len( power_set )

if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 29 solution is:",  e29()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


