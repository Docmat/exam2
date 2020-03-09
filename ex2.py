a=[1,2,3]
b=[11,22,33]

def comb(a,b):
    s = []
    for i in a:
        s.append(i)
        s.append(b[a.index(i)])
    return s

print(comb(a,b))
