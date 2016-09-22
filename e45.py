
import time

def e45():
    pentagon_set = set()
    pentagon_hash = {}

    n,p = 0,0 
    while True:
        p += 3*n + 1
        if pentagon_hash.has_key( p ):
            return pentagon_hash[p]
        
        for smaller_p in pentagon_set:
            diff = p - smaller_p
            if diff in pentagon_set:
                pentagon_hash[ p + smaller_p ] = diff

        pentagon_set.add( p )
        n += 1  

if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 45 solution is:",  e45()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),
    print


