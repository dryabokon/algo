import numpy
# ----------------------------------------------------------------------------------------------------------------------
def count_number_of_ways2(N,steps=[1,2]):

    D = numpy.zeros(N,dtype=numpy.int)
    for step in steps:
        D[step-1]=1

    for n in range(N):
        for step in steps:
            if n-step>=0:
                if D[n-step]>0:
                    D[n]+=D[n-step]


    print(D)
    return D[-1]
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    n_ways = count_number_of_ways2(5)
    print(n_ways)
