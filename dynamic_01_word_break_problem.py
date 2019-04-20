import  numpy
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
if __name__ == '__main__':
    dictionary = ['apple', 'bar', 'bear', 'book', 'dog']
    string = 'bearbook'

    word_break(dictionary, string)



