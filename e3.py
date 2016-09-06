

import time

def e3():
    test_number = 600851475143

    max_prime = 0
    primes = [2]
    current_counter = 3

    while True:
        is_prime = True
        for p in primes:
            if p ** 2 > current_counter:
                break
            if current_counter % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append( current_counter )
            while test_number % current_counter == 0:
                max_prime = current_counter
                test_number /= current_counter
        
        if test_number == 1:
            break

        current_counter += 1


    return max_prime



if __name__ == "__main__":
    start = time.time()
    # print
    print
    print "Euler 3 solution is:",  e3()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


