#!/usr/bin/python
#coding:utf-8
## quick sort
# author: evenhh 
# date: 2019-11-27
# quick sort and find the k largest number


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
    # 取第一个元素做为基准值
    temp = a[l]
    i = r
    j = l

    # 判断左右2个哨兵的值
    # 如果有左边哨兵值大于基准值并且右边哨兵值小于基准值则交换，然后左边哨兵前进，右边哨兵后退，直到2者相遇
    while j < i:
        if  a[j] > temp:
            while i > j:
                if a[i] <= temp:
                    s = a[i]
                    a[i] = a[j]
                    a[j] = s
                    i = i-1
                    break
                i = i-1
        j = j + 1

    # 判断右哨兵节点是否比基准值大，如果大，那么交换基准值与右边哨兵前一个元素（哨兵前一个元素一定不大于基准值)
    # 反之则交换基准值与左哨兵值
    if a[i] > temp:
        a[l] = a[i-1]
        a[i-1] = temp
        print(a)
        return i - 1
    else:
        a[l] = a[j]
        a[j] = temp
        print a
        return j



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

    q = partion_k(a,p,r,k)

    if q == k:
        return 
    if q > k :
        find_K(a,p,q-1,k)
    if q < k:
        find_K(a,q+1,r,k)


def partion_k(a,l,r,k):
    # 取第k元素做为基准值
    temp = a[l]
    i = r
    j = l

    # 判断左右2个哨兵的值
    # 如果有左边哨兵值大于基准值并且右边哨兵值小于基准值则交换，然后左边哨兵前进，右边哨兵后退，直到2者相遇
    while j < i:
        if  a[j] > temp:
            while i > j:
                if a[i] <= temp:
                    s = a[i]
                    a[i] = a[j]
                    a[j] = s
                    i = i-1
                    break
                i = i-1
        j = j + 1
    if a[i] > temp:
        a[l] = a[i-1]
        a[i-1] = temp
        return i - 1
    else:
        a[l] = a[j]
        a[j] = temp
        return j





if __name__ == "__main__":
    #quick_sort(a,0,len(a)-1)
    print(a)
    find_K(a,0,len(a)-1,10)
    print(a[10])
    




