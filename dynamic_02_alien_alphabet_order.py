import  numpy
# ----------------------------------------------------------------------------------------------------------------------
# Given array of sorted words, find order (or precedence of characters) in the language
# ['apple','bear','book',dog']
# ----------------------------------------------------------------------------------------------------------------------
def build_dict(list_of_words):
    dict = {}

    for word in list_of_words:
        for key in word:
            dict[key] = 0

    return list(dict.keys())
# ----------------------------------------------------------------------------------------------------------------------
def find_precedence(list_of_words):

    list_of_keys = build_dict(list_of_words)
    print(' '.join(list_of_keys),'\n')
    K = len(list_of_keys)

    idx = {}
    for each,i in zip(list_of_keys,numpy.arange(0,K,1)):
        idx[each]=i

    edge = numpy.zeros((K,K),dtype=numpy.int)

    for i in range(0,len(list_of_words)-1):
        for j in range(i+1, len(list_of_words)):
            word1 = list_of_words[i]
            word2 = list_of_words[j]
            i1,i2=0,0
            while i1<len(word1) and i2<len(word2) and word1[i1]==word2[i2]:
                i1,i2=i1+1,i2+1
            if i1<len(word1) and i2<len(word2):
                #if edge[idx[word1[i1]],idx[word2[i2]]]==0:
                    #print(word1[i1],'<',word2[i2])
                edge[idx[word1[i1]],idx[word2[i2]]]=1

    edge2 = edge.copy()
    flag = 1
    while flag==1:
        flag = 0
        for i1 in range(0,K-2):
            for i2 in range(i1, K - 1):
                for i3 in range(i2, K - 3):
                    if edge2[i1,i2]>0 and edge2[i2,i3]>0:
                        if edge2[i1,i3]==0:
                            edge2[i1,i3]=1
                            flag =1

    S = numpy.sum(edge2,axis=1)
    idx = numpy.argsort(-S)

    #print(' '.join(numpy.array(list_of_keys)[idx]))

    for s in numpy.unique(S)[::-1]:
        idx = numpy.where(S==s)
        print(' '.join(numpy.array(list_of_keys)[idx]))
    return
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    text= 'Python is an interpreted, high-level, general-purpose programming language. ' \
          'Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code ' \
          'readability, notably using significant whitespace. It provides constructs that enable clear programming on both ' \
          'small and large scales. Van Rossum led the language community until July 2018. Python is dynamically typed ' \
          'and garbage-collected. It supports multiple programming paradigms, including procedural, object-oriented, ' \
          'and functional programming. Python features a comprehensive standard library, and is referred to as batteries included. ' \
          'Python interpreters are available for many operating systems. CPython, the reference implementation of Python, ' \
          'is open-source software and has a community-based development model. ' \
          'Python and CPython are managed by the non-profit Python Software Foundation.'

    text = text.replace('-', '')
    text = text.replace(',', '')
    text = text.replace('.', '')
    for each in ['0','1','2','3','4','5','6','7','8','9']:
        text = text.replace(each, '')

    list_of_words = numpy.sort(list(set(text.lower().split())))
    #list_of_words = ['apple', 'bar', 'bear', 'book', 'dog']

    find_precedence(list_of_words)





