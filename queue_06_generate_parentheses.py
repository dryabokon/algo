import numpy
# ----------------------------------------------------------------------------------------------------------------------
def generate_parentheses(N):

    q = [('(',N-1,N)]
    res = []

    while len(q)>0:

        element=q.pop()
        if len(element[0])==2*N:
            res.append(element[0])

        spent1 = N - element[1]
        spent2 = N - element[2]
        open = spent1-spent2
        to_spend = 2*N- spent1- spent2
        #try '('
        if element[1]>0 and open<=to_spend:
            new_element=(element[0]+'(',element[1]-1,element[2])
            q.append(new_element)
        # try ')'
        if element[2]>0 and element[1]<element[2]:
            new_element = (element[0] + ')', element[1], element[2]-1)
            q.append(new_element)


    return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    res = generate_parentheses(2)
    for each in res:
        print(each)




