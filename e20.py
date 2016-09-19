
import time

def e20():
    mult = lambda  x, y: x*y
    fac_100  = reduce( mult, xrange(1, 100), 1 )
    current_digit_sum = 0
    for c in str( fac_100 ):
        current_digit_sum += int(c)
    return current_digit_sum 

if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 20 solution is:",  e20()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),
    print
