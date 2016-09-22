
import time

def e45():
    trianges = { i * (i+1) / 2 for i in xrange(1,100000) }
    pentagons = { i * (3*i-1) / 2 for i in xrange(1,100000) }
    hexagons = { i * (2*i-1) for i in xrange(1,100000) }

    return sorted( list(trianges & pentagons & hexagons) )[2]

if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 45 solution is:",  e45()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),
    print
