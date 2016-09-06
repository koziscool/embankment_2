

import time

def is_palindrome( n ):
    str_n = str(n)
    len_str_n = len( str_n )

    for i in xrange( len_str_n / 2):
        if str_n[i] != str_n[ len_str_n - i -1]:
            return False

    return True


def e4():
    max_pal = 0
    for i in xrange( 100, 1000 ):
        for j in xrange( i+1, 1000 ):
            if is_palindrome( i*j ) and i*j > max_pal:
                max_pal = i*j
    return max_pal


if __name__ == "__main__":
    start = time.time()
    # print
    print
    print "Euler 4 solution is:",  e4()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),



