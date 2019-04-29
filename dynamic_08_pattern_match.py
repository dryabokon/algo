import numpy
# ----------------------------------------------------------------------------------------------------------------------
# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
def isMatch(text, pattern):
    """
        :type s: str
        :type p: str
        :rtype: bool
        """

    LT = len(text)
    LP = len(pattern)

    if len(text)==0:
        return True

    A = numpy.full((LT,LP),False)
    A[0,0]=text[0]==pattern[0]

    for t in range(1,LT):
        for p in range(1, LP):
            if pattern[p]=='.' or pattern[p]==text[t]:
                match=1
            else:
                match=0

            A[t, p] = A[t, p] or (A[t-1,p-1] and match)

            if pattern[p]=='*':
                for lookback in range(0,t):
                    array = text[t-lookback+1:t+1]
                    loopback_match = True
                    for each in array:loopback_match = loopback_match and each==pattern[p-1]

                    A[t, p] =A[t, p] or (p==1) or (A[t-lookback, p-2] and loopback_match)

    print(1*A)
    return A[-1][-1]
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':


    res = isMatch('abcd','d*')
    print(res)