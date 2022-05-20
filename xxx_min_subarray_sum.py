#
# ----------------------------------------------------------------------------------------------------------------------
def get_min_subarray_sum(A,s):

    agg = 0
    left =0
    res = float('inf')
    for right in range(len(A)):
        agg+= A[right]
        while(agg>=s):
            res = min(res,right+1-left)
            agg -= A[left]
            left+=1

    if res == float('inf'):
        res=0

    return res
 # ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = [2, 3, 1, 2, 4, 3]
    s = 7

    res = get_min_subarray_sum(A,s)
    print(res)