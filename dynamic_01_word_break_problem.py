# https://thenoisychannel.com/2011/08/08/retiring-a-great-interview-problem
import numpy
# ----------------------------------------------------------------------------------------------------------------------
# Given a dictionary of words, find if string can be split into words
# ----------------------------------------------------------------------------------------------------------------------
def get_start_stop(dictionary,string):
    A = []

    for k in range(0,len(dictionary)):
        L = len(dictionary[k])
        for i in range(0,len(string)-L+1):
            if string[i:i+L]==dictionary[k]:
                A.append((k,i,i+L-1))

    return numpy.array(A)
# ----------------------------------------------------------------------------------------------------------------------
def word_break(dictionary,string):


    A = get_start_stop(dictionary,string)
    print(A)
    print('------------')
    for each in A:
        print(' '*each[1],end='')
        for n in range (each[1],each[2]+1):print(each[0],end='')
        print()

    print('------------')
    L = len(string)
    D = numpy.full(L ,-1)

    for each in A:
        if each[1]==0:
            D[each[2]]=each[0]

    for i in range(1,L):
        for each in A:
            if each[2]==i and i-(each[2]-each[1]+1)>=0 and D[i-(each[2]-each[1]+1)]>=0:
                D[i]=each[0]

    print(D)

    res=[]
    i,k=L-1,D[i]
    while i>=0 and k>=0:
        res.append(dictionary[k])
        i-=len(dictionary[k])
        k=D[i]

    for i in reversed(range(0,len(res))):
        print(res[i],end=' ')

    return
# ----------------------------------------------------------------------------------------------------------------------
def segment_string(A, dct):

    if A in dct:
        return A

    for i in range(1, len(A)):
        prefix = A[:i]
        if prefix in dct:
            suffix = A[i:len(A)]
            segSuffix = segment_string(suffix, dct)
            if len(segSuffix)>0:
                return prefix + " " + segSuffix
    return []
# ----------------------------------------------------------------------------------------------------------------------
def segment_string2(A, dct,memorized):

    if A in dct:
        return A

    if A in memoized:
        return memoized[A]

    for i in range(1, len(A)):

        prefix = A[:i]
        if prefix in dct:
            attempt = segment_string2(A[i:], dct,memorized)
            if attempt!=[]:
                memoized[A] = prefix + " " + attempt
                return prefix + " " + attempt

    memoized[A]= 0
    return []

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    dictionary = ['apple', 'bar', 'bear', 'book', 'dog']
    string = 'bearbookbearbook'
    #string ="catsandog"
    #dictionary  = ["cats", "dog", "sand", "and", "cat"]

    memoized = {}
    res = segment_string2(string,dictionary,memoized)
    print(res)
