# https://leetcode.com/problems/summary-ranges/
# ----------------------------------------------------------------------------------------------------------------------
def ranges(A):

    prev = A[0]
    starts = [A[0]]
    stops = [A[0]]

    for a in A[1:]:
        if a-prev==1:
            #extend current range
            stops[-1]=a
        else:
            #start new range
            starts.append(a)
            stops.append(a)
        prev=a

    res = []
    chr1 = '"'
    for start,stop in zip(starts,stops):
        if start==stop:
            value = '%s%s%s'%(chr1,start,chr1)
        else:
            value = '%s%s->%s%s'%(chr1,start,stop,chr1)
        res.append(str(value))

    return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = [0,1,2,4,5,7]


    res = ranges(A)
    for r in res:
        print(r)