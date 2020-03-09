def fib():
    l = [1,1]
    while len(l) <= 100:
        l.append(l[-2]+l[-1])
    return l

print(fib())
# def fib(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
#
# print(fib())
