# https://leetcode.com/problems/maximum-product-of-word-lengths/
# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.
# ----------------------------------------------------------------------------------------------------------------------
def wrd_len(words):

    mask = [0]*len(words)
    for i,w in enumerate(words):
        for c in set(w):
            mask[i] |= (1 << (ord(c) - ord('a')))

    res = 0
    for i in range(0,len(words)-1):
        for j in range(i, len(words)):
            if mask[i]&mask[j]==0:
                res = max(res,len(words[i])*len(words[j]))

    return res
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    res = wrd_len(words)
    print(res)
