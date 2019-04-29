import numpy
# ----------------------------------------------------------------------------------------------------------------------
def find_open_close(list_of_symbols):
    L = len(list_of_symbols)
    c = numpy.zeros(L,dtype=numpy.int)
    cnt=0
    max=0
    start=0
    for i in range(0,L):
        if list_of_symbols[i]=='{':
            cnt+=1
        if list_of_symbols[i]=='}':
            cnt-=1
        c[i]=cnt
        if cnt>max:
            max=cnt
            start=i

    i=start
    while(i<L) and c[i]==max:
        i+=1
    stop=i

    return start,stop
# ----------------------------------------------------------------------------------------------------------------------
 # abc{ABC}da{AB{KL}}
def generate_from_string(list_of_symbols):

    pos_open,pos_close = find_open_close(list_of_symbols)
    prefix = list_of_symbols[:pos_open]
    suffix = list_of_symbols[pos_close+1:]
    result = []
    for i in range(pos_open+1,pos_close):
        res = []
        for each in prefix: res.append(each)
        res.append(list_of_symbols[i])
        for each in suffix:res.append(each)
        result.append(''.join(res))
    return result
# ----------------------------------------------------------------------------------------------------------------------
def genarate_queue(queue):

    while (len(queue) > 0):
        value = queue.pop()
        if '{' in value:
            next_gen = generate_from_string(list(value))
            for each in next_gen:queue.append(each)
        else:
            print(value)
    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    A = list('abc{123}de{XY}{+-}')
    genarate_queue([A])



