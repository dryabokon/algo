def heapify_PQ_node(keys,values,i):

    N = len(keys)
    left  = 2 * (i + 1) - 1
    right = 2 * (i + 1) + 1 - 1
    largest = i
    if left <N and (keys[left ]>keys[largest]):largest = left
    if right<N and (keys[right]>keys[largest]):largest = right

    if largest!=i:
        keys[largest],keys[i]=keys[i], keys[largest]
        values[largest], values[i] = values[i], values[largest]
        heapify_PQ_node(keys,values,largest)

    return
# ----------------------------------------------------------------------------------------------------------------------
def build_PQ(keys,values):
    L = len(keys)
    for i in reversed(range(0,L//2)):
        heapify_PQ_node(keys,values,i)
    return
# ----------------------------------------------------------------------------------------------------------------------
def merge_sorded(A0,A1,A2,A3):

    result = []

    L0,L1,L2,L3 = len(A0),len(A1),len(A2),len(A3)

    keys = [A0[0], A1[0], A2[0], A3[0]]
    idx  = [1,1,1,1]
    values = [0,1,2,3]

    build_PQ(keys,values)

    while(len(keys)!=0):

        result.append(keys[0])
        key,value = None,None
        if values[0] == 0 and idx[0]<L0: key, value, idx[0] = A0[idx[0]],0,idx[0]+1
        if values[0] == 1 and idx[1]<L1: key, value, idx[1] = A1[idx[1]],1,idx[1]+1
        if values[0] == 2 and idx[2]<L2: key, value, idx[2] = A2[idx[2]],2,idx[2]+1
        if values[0] == 3 and idx[3]<L3: key, value, idx[3] = A3[idx[3]],3,idx[3]+1
        if key is not None:
            keys[0],values[0]=key,value
            heapify_PQ_node(keys,values,0)

        else:
            keys[0],values[0]=keys[-1],values[-1]
            del(keys[-1])
            del(values[-1])


    return result

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A0 = list('999876')
    A1 = list('7654')
    A2 = list('987651')
    A3 = list('543')

    res = merge_sorded(A0,A1,A2,A3)
    print(''.join(res))



