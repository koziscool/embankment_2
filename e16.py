

import time

def e16():
    sum_digits = 0
    for c in str( 2 ** 1000 ):
        sum_digits += int(c)
    return sum_digits

if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 16 solution is:",  e16()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


