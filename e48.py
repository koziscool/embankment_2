
import time

def e48():
    current_sum, end_range = 0, 1000

    # def self_power(i):
    #     current_addend, current_sum = i, 0
    #     for _ in xrange(1, i ):
    #         current_addend *= i
    #     current_sum +=  current_addend % (10 ** 10)
    #     return current_sum

    # add_self_power = lambda i, j: self_power(i) + self_power(j) 
    # return reduce(  add_self_power, xrange(1, 1001), 0) 

    for i in xrange(1, end_range + 1 ):
        current_addend = i
        # self_power = lambda 
        for _ in xrange(1, i ):
            current_addend *= i
        current_sum +=  current_addend % (10 ** 10)

    return current_sum % (10 ** 10)


if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 48 solution is:",  e48()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),
    print
