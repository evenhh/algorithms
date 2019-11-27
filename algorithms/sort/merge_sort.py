#!/usr/bin/python
#coding:utf-8
# author: evenhh 
# date: 2019-11-27
# merge sort 

import random
import time

def merge_sort(a):
    if len(a)<=1:
        return a
    d = len(a)/2
    left = merge_sort( a[:d] )
    right = merge_sort( a[d:] )
    return merge(left,right)


def merge(a,b):
    temp = []
    i = j = 0
    while i<len(a) and  j<len(b):
        if a[i]<b[j]:
            temp.append(a[i])
            i = i + 1 
        else:
            temp.append(b[j])
            j = j + 1
    if i == len(a):
        for e in b[j:]:
            temp.append(e)
    else:
        for e in a[i:]:
            temp.append(e)

    return temp



if __name__ == "__main__":

    arr = [23,22,20,12,3,5,6,7,8,10,12,14]

    print merge_sort(arr)
    i = 0
    random_arr = []
    while i<10000:
         random_arr.append(random.randint(0,10000))
         i = i +1 
    
    start  = time.time()
    merge_sort(random_arr)
    print (time.time() - start)*1000
    print time.time()








