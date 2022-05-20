# Given an array, rotate the array to the right by k steps, where k is non-negative.
# ----------------------------------------------------------------------------------------------------------------------
def roll_array(A,k):

    # S = len(A)-(k+len(A))%len(A)
    # for step in range(S):
    #     for i in range(1,len(A)):
    #         A[i],A[i-1] = A[i-1],A[i]

    n = len(A)
    k = k % n
    A[:] = A[n - k:] + A[:n - k]
    return

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7]
    #A = [1, 2]
    k = 3



    roll_array(A,k)
    print(A)