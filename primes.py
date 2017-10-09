#!/usr/bin/env python3

import math

def eratosthenes(n):
    all_num=list(range(2,n))
    for i in range(2, math.ceil(math.sqrt(n))):
        all_num = list(filter(lambda x: (x%i != 0 or x == i) , all_num))
    return all_num

def main():
    args = sys.argv
    n=int(args[1])
    print(eratosthenes(n))
    
if __name__ == "__main__":
    main(sys.argv)
    