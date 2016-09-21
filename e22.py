

import time

def e22():
    letter_values = {  'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
                            'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,
                            'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26 }

    file_name = 'p022_names.txt'
    f = open(file_name, 'r')
    names = map( lambda n: n.strip('"'), sorted( f.readline().split(",") ) )
    accumulator = 0
    for i, name in enumerate(names):
        for c in name:
            accumulator += (i+1) * letter_values[c]

    return accumulator



if __name__ == "__main__":
    start = time.time()
    print
    print "Euler 22 solution is:",  e22()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start)),


