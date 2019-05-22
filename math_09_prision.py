# ----------------------------------------------------------------------------------------------------------------------
import numpy
# ----------------------------------------------------------------------------------------------------------------------
def reclc_state(A):
    B=[0]*len(A)
    for i in range(1,len(A)-1):
        B[i]=1*(A[i-1]==A[i+1])
    B[0]=0
    B[-1]=0
    for i in range(0,len(A)):
        A[i]=B[i]

    return
# ----------------------------------------------------------------------------------------------------------------------
def to_hex(A):
    res = 0
    for each in A:
        res=res<<1
        if each>0:
            res+=1

    return res
# ----------------------------------------------------------------------------------------------------------------------
def prison_after_N_days(A, N):

    first_appearence={}
    increment ={}

    n=0
    while n <N:
        key = to_hex(A)
        if key not in first_appearence:
            first_appearence[key] = n
            reclc_state(A)
            n += 1
        else:
            if key not in increment:
                increment[key]=n-first_appearence[key]
                reclc_state(A)
                n += 1
            else:
                if False and n+increment[key]<N:
                    mul = (N-n)//increment[key]
                    n+=increment[key]*mul
                else:
                    reclc_state(A)
                    n += 1

    return A
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':


    A=[1, 0, 0, 1, 0, 0, 1, 0]


    A = prison_after_N_days(A, 1000000000)
    print('-----------')
    print(A)


