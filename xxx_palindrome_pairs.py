# https://leetcode.com/problems/palindrome-pairs/
# Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.
# ----------------------------------------------------------------------------------------------------------------------
def palindrome_pairs(words):

    def is_palindrome(word):return word == word[::-1]

    res = []
    for i1 in range(len(words)):
        for i2 in range(len(words)):
            if i1==i2:continue
            if is_palindrome(words[i1]+words[i2]):
                res.append([i1,i2])

    return res

# ----------------------------------------------------------------------------------------------------------------------
def palindrome_pairs2(words):

    dct_words = {word: i for i, word in enumerate(words)}
    res = []
    for word, k in dct_words.items():
        n = len(word)
        for j in range(n + 1):
            pref = word[:j]
            suf = word[j:]
            if pref==pref[::-1]:
                back = suf[::-1]
                if back != word and back in dct_words:
                    res.append([dct_words[back], k])
            if j != n and suf==suf[::-1]:
                back = pref[::-1]
                if back != word and back in dct_words:
                    res.append([k, dct_words[back]])
    return res
# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':

    words = ["abcd","dcba","lls","s","sssll"]

    res = palindrome_pairs2(words)
    print(res)
