import numpy
# ----------------------------------------------------------------------------------------------------------------------
#get all subsets of a set.
def get_all_subsets(array):
    N=array.shape[0]

    for i in range(0,2**N):
        idx = numpy.array([(i>>b)&1 for b in range(0,N)])
        print(array[numpy.where(idx>0)])

    return

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = numpy.array(list('5672'))

    get_all_subsets(A)
