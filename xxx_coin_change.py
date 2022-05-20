# https://leetcode.com/problems/coin-change/
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# ----------------------------------------------------------------------------------------------------------------------
def coin_change(coins, amount):

    if amount==0:
        return 0

    queue = [(amount,[])]
    res = []

    while len(queue)>0:
        x = queue.pop()
        current_ammount = x[0]
        current_change = x[1]
        print(queue)

        for c in coins:
            if c==current_ammount:
                res.append(current_change+[c])
            elif current_ammount-c>0:
                queue.append((current_ammount-c,current_change+[c]))

    if len(res)==0:
        return -1
    else:
        return min([len(r) for r in res])

# ----------------------------------------------------------------------------------------------------------------------
def coin_change2(coins, amount):

    need = [float('Inf')]*(amount+1)
    need[0]=0

    for a in range(amount+1):
        for c in coins:
            if a-c>=0:
                need[a] = min(need[a],1+need[a-c])

    print(need)
    if need[-1]!=float('Inf'):
        return need[-1]
    else:
        return -1


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    coins = [2,5,10,1]
    amount = 27
    res = coin_change2(coins, amount)
    print(res)
