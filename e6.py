

import time

def e6():
    end_range = 100
    sum_squares = sum( i*i for i in xrange(1, end_range+1 ))
    square_sum = pow( sum(xrange(1, end_range + 1)), 2)

    return  square_sum - sum_squares

if __name__ == "__main__":
    start = time.time()
    # print
    # print
    print "Euler 6 solution is:",  e6()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


