
import time

def e48():
    current_sum, end_range = 0, 1000
    for i in xrange(1, end_range + 1 ):
        current_addend = i
        for _ in xrange(1, i ):
            current_addend *= i
        current_sum +=  current_addend % (10 ** 10)

    return current_sum % (10 ** 10)


if __name__ == "__main__":
    start = time.time()
    print "Euler 48 solution is:",  e48()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),
    print
