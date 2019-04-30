# ----------------------------------------------------------------------------------------------------------------------
def sign(x):
    if x>0:
        return +1
    elif x<0:
        return -1
    else: return 0
# ----------------------------------------------------------------------------------------------------------------------
def zigzag(A):

    flag =+1
    for i in range(1,len(A)):
        if sign(ord(A[i])-ord(A[i-1]))*flag==1:
            A[i],A[i-1] = A[i-1],A[i]
        flag*=-1

    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list(set(list('2623447456234597234871298371334584')))

    print(''.join(A))

    zigzag(A)
    print(''.join(A))
