def bucket_sort(A):

    L = len(A)
    value_min,value_max = ord(min(A)), ord(max(A))

    bucket = [[]for i in range(value_min,value_max+1) ]

    for i in range(0,L):
        bucket[ord(A[i])-value_min].append(A[i])

    result=[]
    for i in range(value_min, value_max + 1):
        for j in range(0,len(bucket[i-value_min])):
            result.append(bucket[i-value_min][j])

    for i in range(0,L):
        A[i]=result[L-1-i]

    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('2623447456234584')
    B = list(map(int, A))

    print(''.join(A))

    bucket_sort(A)
    print(''.join(A))

