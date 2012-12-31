#!/usr/bin/env python
import sys
from array import array
import random
import time
import hmm_faster

def main():
    
    hmm_train = hmm_faster.HMM()
    hmm_train.set_states([0, 1])
    obs = [chr(x) for x in xrange(ord('A'), ord('Z') + 1)]
    obs.append(" ")
    hmm_train.set_observations(obs)
    hmm_train.randomize_matrices(1123)
    
    finput = open("hmm-train.clean.txt", 'r')
    for line in finput:
        line = line.replace("\n", "")
        hmm_train.train(line[:1000])
        
    finput.close()
    
    sys.exit(0)
    
    N = 100000000
    li = [0 for i in xrange(N)]
        
    start_time = time.time()
    a = 0
    for i in xrange(N):
        a = i
    end_time = time.time()
    print (end_time - start_time)
    
    start_time = time.time()
    a = 0
    idx = 0
    for i in xrange(len(li)):
        a = i
    end_time = time.time()
    print (end_time - start_time)
    
    sys.exit(0)
    
    mylist = list([0] * N)
    # myarr = array('f', mylist)
    mydict = dict()
    for i in xrange(0, N):
        mydict[(i,i * 2, "p")] = 0
    
    start_time = time.time()
    for i in xrange(0, N):
        rnd = random.random()
        # myarr.append(rnd)
        mydict[(i,i * 2, "p")] = rnd        
    end_time = time.time()
    print (end_time - start_time)

    start_time = time.time()
    for i in xrange(0, N):
        rnd = random.random()
        # myarr.append(rnd)
        mylist[i] = rnd
    end_time = time.time()
    print (end_time - start_time)
    
    sys.exit(0)
    
    start_time = time.time()
    for i in xrange(0, 10000000):
        rnd = random.random()
        myarr.append(rnd)        
    end_time = time.time()
    print (end_time - start_time)
    
    start_time = time.time()
    for i in xrange(0, 10000000):
        rnd = random.random()
        mylist.append(rnd)        
    end_time = time.time()
    print (end_time - start_time)
    

if __name__ == "__main__":
    main()