t = [1,2,4,7,8,0]


def sum(numbers):
    num = 0
    for n in numbers :
        num += n
    return num

# sum(numbers)



def sum2(numbers):
    num = 0
    n = len(numbers)
    while n:
        n -= 1
        num += numbers[n]
    return num



def sum3(numbers):
    if len(numbers) == 0:
        return 0
    else:
        numbers[0] + sum (numbers[1:])




print(sum(t))
print(sum2(t))
print(sum3(t))
