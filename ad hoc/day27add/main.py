def add(*args):
    result = 0
    #for number in args:
    #    result = result + number # result += number
    result = sum(args)
    return result


sum_number = add(1, 2, 3, 4, 5)
print(sum_number)
