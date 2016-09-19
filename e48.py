
import time
import operator

def e48():
    def self_power(i):
        current_addend = i 
        for _ in xrange(1, i ):
            current_addend *= i
            current_addend %= (10 ** 10)
        return current_addend

    self_powers = map( self_power, xrange(1, 1001) )
    return reduce(  operator.add, self_powers ) % (10 ** 10)

if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 48 solution is:",  e48()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),
    print
