#!/usr/bin/python
#coding:utf-8
## quick sort
# author: evenhh 
# date: 2019-11-27
# quick sort and find the k largest number

import time
import random



a = [8,9,6,3,5,1,2,4,7,11,10]



def quick_sort(a,p,r):
    if p >= r:
        return
   # 分区
    q = partion(a,p,r)
    # 左分区
    quick_sort(a,p,q-1)
    # 右分区
    quick_sort(a,q+1,r)

# 分区及交换
def partion(a,l,r):
    
    # 默认取第一个元素
    guard = a[l]
    

    # 当左边游标小于右边游标时
    while l < r:
        # 从右边找到一个小于guard的下标，并放置到左边游标的位置(首次操作占据guard值的下标)
        while l < r and a[r] >= guard:
            r = r - 1
        a[l] = a[r]
        # 从左边找一个大于guard的下标，然后存放到右边游标的位置
        while l < r and a[l] < guard:
            l = l + 1 
        a[r] = a[l]
    # 循环结束后2个游标相遇，此时的下标即为下次递归的分界点
    a[l] = guard
    return l 



'''
    基于快排，查找数组第K大元素
    思路：
        选择一个基准值，每次做分区操作，获取下标，如果下标是K-1则返回值
        如果不是，判断下标值，递归分区

'''


def find_K(a,p,r,k):
    if p >= r:
        # print  p
        # print "enda"
        return 
    q = partion(a,p,r)

    if q == k-1:
        return 
    if q > k-1 :
        find_K(a,p,q-1,k-1)
    if q < k-1:
        find_K(a,q+1,r,k-1)

if __name__ == "__main__":    
    i =j= 0
    random_arr = []
    random_arr2 = []#[9,8,7,6,5,3,4,2,1,0]
    while i<10000:
         random_arr.append(random.randint(0,10000))
         i = i +1 
    while j < 10:
        random_arr2.append(random.randint(0,100))
        j = j +1 
    start  = time.time()
    quick_sort(random_arr,0,9999)
    print (time.time() - start)*1000
   
    
    print "xxx"
    print(len(random_arr2))
    start  = time.time()
    r = random.randint(0,9)
 
    find_K(random_arr2,0,9,7)
    print (time.time() - start)*1000
    print r,"\n",random_arr2
 
    quick_sort(random_arr2,0,9)
    print random_arr2