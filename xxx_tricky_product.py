# https://leetcode.com/problems/product-of-array-except-self/
# Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# ----------------------------------------------------------------------------------------------------------------------
def product(A):

    cnt=0

    P = 1
    for a in A:
        if a==0:
            cnt+=1
        else:
            P*=a

    if cnt>=2:
        res = [0 for a in A]
    elif cnt==1:
        res = [0 if a!=0 else P for a in A]
    else :
        res = [int(P/a) for a in A]

    return res
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    A = [1,2,3,4]

    res = product(A)
    print(res)