
import time

def e40():
    end_range = 10 ** 6
    digit_str = "".join( str(i) for i in xrange(1, end_range) )
    return ( int(digit_str[0]) * int(digit_str[9]) * int(digit_str[99]) * 
        int(digit_str[999]) * int(digit_str[9999]) * int(digit_str[99999]) * int(digit_str[999999]) )


if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 40 solution is:",  e40()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),
    print
