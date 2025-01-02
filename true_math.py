from math import inf
def divide(first, second):
    if second == 0:
        return f'{first}/{second} = {inf}'
    else:
        res = round(first / second,2)
        return f'{first}/{second} = {res}'