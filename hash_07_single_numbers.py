# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
# Find the two elements that appear only once. You can return the answer in any order.
# ----------------------------------------------------------------------------------------------------------------------
def SN(A):

    dct = {}
    for a in A:
        if a in dct:
            dct[a]+=1
        else:
            dct[a]=1

    res = []
    for k,v in dct.items():
        if v==1:
            res.append(k)

    return res
# ----------------------------------------------------------------------------------------------------------------------
def SN3(A):

    xor_value = 0
    for a in A:
        xor_value ^= a

    rightmost_bit_mask = 1

    while (rightmost_bit_mask & xor_value) == 0:
        rightmost_bit_mask <<= 1

    num1, num2 = 0, 0

    for a in A:
        if (a & rightmost_bit_mask):
            num1 ^= a
        else:
            num2 ^= a
    return [num1, num2]
# ----------------------------------------------------------------------------------------------------------------------
def SN4(A):
    xor_value=0
    value1,value2 = 0,0

    for each in A:
        xor_value^=(each)

    rightmost_bit_mask = xor_value & (~(xor_value-1))

    for each in A:
        if (each)&rightmost_bit_mask == rightmost_bit_mask:
            value1 ^= (each)
        else:
            value2 ^= (each)

    return [(value1),(value2)]
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    A = [-1,-1,1, 2, 1, 3, 2, 5]
    res =SN4(A)

    print(res)