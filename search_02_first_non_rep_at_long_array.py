# store both: count + first occurrence
# ----------------------------------------------------------------------------------------------------------------------
def first_unique_symbol(A):

    count ={}
    pos={}

    for i,symbol in enumerate(A):
        if symbol in count:
            count[symbol] += 1
        else:
            count[symbol] = 1
            pos[symbol] = i

    for key, num in count.items():
        if num==1:
            return key

    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    A = list('765dgdfglk7jlkjf34lk5j45l6kjlkdflgkj123')

    res = first_unique_symbol(A)
    print(res)
