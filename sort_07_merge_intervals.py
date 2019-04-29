# ----------------------------------------------------------------------------------------------------------------------
import numpy
# ----------------------------------------------------------------------------------------------------------------------
def merge(A):

    A = numpy.sort(A,axis=0)

    result = []
    for interval in A:
        # no_overlap(current, prev) => append current
        if len(result)==0 or result[-1][1] < interval[0]:
            result.append(interval)
        else:
        # merge (current,prev)
            result[-1][1]= max(result[-1][1], interval[1])

    return result
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A =  [[1,3],[2,6],[8,10],[15,18]]

    res = merge(A)
    for each in res:
        print(each)

