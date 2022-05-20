# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
# https://leetcode.com/problems/house-robber/
# ----------------------------------------------------------------------------------------------------------------------
def house_robber(A):
    N = len(A)
    V = [a for a in A]

    for i in range(2,N):
        max_prev = max(V[:i - 1])
        V[i]+= max_prev

    return max(V)

# ----------------------------------------------------------------------------------------------------------------------
def house_robber_fast(X):
    prev = cur = 0
    for x in X:
        prev, cur = cur, max(prev + x, cur)
        print(prev, cur)

    return cur
# ----------------------------------------------------------------------------------------------------------------------
#All houses at this place are arranged in a circle
def house_robber_circle(X):
    max(house_robber(X[1:]), house_robber(X[:-1]))
    return
# ----------------------------------------------------------------------------------------------------------------------

def house_robber_circle_fast(X):

    a = b = c = d = 0
    for i in range(len(A) - 1):
        a, c, b, d = b, d, max(b, a + X[i]), max(d, c + X[i + 1])
    return max(b, d, X[0])

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    A = [2,3,2]

    res = house_robber_circle(A)
    print(res)