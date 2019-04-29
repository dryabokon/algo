import numpy
# ----------------------------------------------------------------------------------------------------------------------
mapping = {}
mapping['2'] = 'abc'
mapping['3'] = 'def'
mapping['4'] = 'ghi'
mapping['5'] = 'jkl'
mapping['6'] = 'mno'
mapping['7'] = 'pqrs'
mapping['8'] = 'tuv'
mapping['9'] = 'wxyz'
# ----------------------------------------------------------------------------------------------------------------------
digits = list('23456789')
# ----------------------------------------------------------------------------------------------------------------------
def generate_phone_string(digits_string):

    q = [digits_string]
    res = []

    while len(q)>0:
        pattern  = q.pop(0)
        flag_res = True
        for digit in digits:
            if digit in pattern:
                flag_res = False
                idx = pattern.index(digit)
                upsample = mapping[digit]
                for l in range(0,len(upsample)):
                    new_pattern = pattern[:idx]+upsample[l]+pattern[idx+1:]
                    q.append(new_pattern)
                break
        if flag_res==True:
            res.append(pattern)


    return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':


    res = generate_phone_string('23')
    for each in res:
        print(each)



