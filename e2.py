

import time

def e2():
    fibo = [1, 2]
    sum_evens = 0
    while fibo[-1]< 4 * 10 ** 6:
        if fibo[-1] % 2 == 0:
            sum_evens += fibo[-1]

        fibo.append( fibo[-1] + fibo[-2] )

    return sum_evens


if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 2 solution is:",  e2()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


