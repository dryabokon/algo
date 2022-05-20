# Given a dictionary of words, find if string can be split into words
# https://thenoisychannel.com/2011/08/08/retiring-a-great-interview-problem
# ----------------------------------------------------------------------------------------------------------------------
def segment_string(A, dct):

    if A in dct:
        return A

    for i in range(1, len(A)):
        prefix = A[:i]
        suffix = A[i:]
        if prefix in dct:
            split = segment_string(suffix, dct)

            if split is not None:
                return prefix + ' ' + split

    return None
# ----------------------------------------------------------------------------------------------------------------------
def segment_string_mem(A, dct, memorized):

    if A in dct:
        return A,memorized

    if A in memorized:
        return memorized[A],memorized

    for i in range(1, len(A)):
        prefix = A[:i]
        suffix = A[i:]
        if prefix in dct:
            split,memorized = segment_string_mem(suffix, dct, memorized)

            if split is not None:
                memorized[suffix] = prefix + ' ' + split
                return prefix + ' ' + split, memorized


    return None,memorized
# ----------------------------------------------------------------------------------------------------------------------
# dictionary = ['apple', 'bar', 'bear', 'book', 'dog']
# A = 'bearbookbearbook'

dictionary = ["cats", "dog", "sand", "and", "cat"]
A = "cats"
memorized = {}
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    # res,memorized = segment_string_mem(A, dictionary, memorized)
    # print(res)

    res = segment_string(A,dictionary)
    print(res)

