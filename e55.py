

import time

def e55():
    
    def is_palindrome(n):
        return n == int(str(n)[::-1])

    def reverse_and_add(n):
        return n + int(str(n)[::-1])

    Lychrel_list = []

    for i in xrange( 1, 10**4 ):
        is_Lychrel = True
        current_num = i
        for _ in xrange(50):
            current_num = reverse_and_add( current_num )
            if is_palindrome( current_num ):
                is_Lychrel = False
                break
        if is_Lychrel:
            Lychrel_list.append( i )

    return len( Lychrel_list )

if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 55 solution is:",  e55()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


