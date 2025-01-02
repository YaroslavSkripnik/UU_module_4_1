def divide(first, second):
    if second == 0:
        return f'{first}/{second} = Ошибка (деление на "0")'
    else:
        res = round(first / second,2)
        return f'{first}/{second} = {res}'
