

import time
import operator

def collatz( n, collatz_dict ):
    if n in collatz_dict:
        return collatz_dict[n]
    else:
        if n % 2 == 0:
            answer = 1 + collatz( n/2, collatz_dict )
            collatz_dict[n] = answer
        else:
            answer = 1 + collatz( 3*n + 1, collatz_dict )
            collatz_dict[n] = answer
    return answer


def e14():
    collatz_dict = { 1:1 }

    end_range = 10 ** 6
    for i in xrange( 1, end_range ):
        collatz( i, collatz_dict )

    return max( collatz_dict.iteritems(), key=operator.itemgetter(1) )[0]

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 14 solutions is: ", e14()
    end  = time.time()
    print "elapsed time is %.4f seconds" % (end-start)

