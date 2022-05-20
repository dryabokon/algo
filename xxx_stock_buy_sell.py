#You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions.
# ----------------------------------------------------------------------------------------------------------------------
import numpy


def maxProfit(k,A):

    import numpy
    T = len(A)
    if T<=1:return 0
    if k<=0:return 0

    if k==1:
        if T<2:return 0
        res = [0]
        for split in range(1, T):
            A1, A2 = A[:split], A[split:]
            res.append(max(0,max(A2) - min(A1)))

        res = max(0,max(res))
        return res

    else:
        profit = []
        dbg=[]
        profit.append(maxProfit(k - 1, A))
        dbg.append((k-1,A,0,[]))

        for split in range(1,T):
            A1, A2 = A[:split], A[split:]
            for attempt in range(1, k-1+1):
                profit.append(maxProfit(k-attempt,A1)+maxProfit(attempt,A2))
                dbg.append((k-attempt,A1,attempt,A2))

        # if k==2:
        #     for p,case in zip(profit,dbg):
        #         print(p,case)
            #print(dbg[numpy.argmax(profit)])

        return max(0,max(profit))

# ----------------------------------------------------------------------------------------------------------------------
def maxProfit2(k,A):

    if k==0:
        return 0

    T = len(A)

    if T<=1:
        return 0

    if k>= T/2:
        profit = 0
        for t in range(1, len(A)):
            profit += max(0, A[t] - A[t - 1])
        return profit

    profit = numpy.zeros((k+1,T))

    for kk in range(1,k+1):
        loss=-A[0]
        for t in range(1,T):
            profit[kk][t] = max(profit[kk  ][t - 1]       , A[t] + loss)
            loss          = max(profit[kk-1][t - 1] - A[t],loss)

    return int(profit[k][-1])

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    #A,k = [2,4,1],2
    #A,k = [3, 2, 6, 5, 0, 3],2

    A,k = [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94],7

    res = maxProfit2(k,A)
    print(res)