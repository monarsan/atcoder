n, k = input().split()
k = int(k)

def baseTransform(value: int, base: int)->str:
    next = int(value/base)
    if(next):
        return baseTransform(next, base) + str(value%base)
    return str(value%base)

def eight2five(i: str)->str:
    if i =="8":
        return "5"
    else :
        return i

base10 = 0
for j in range(k):
    r = 1
    for i in range(len(n)):
        base10 += r * int(n[len(n)-i-1])
        r *=8
    n = baseTransform(base10, 9)
    print(n)
    new = ""
    for l in range(len(n)):
        if n[i] =="8":
            new += "5"
        else :
            new += n[l]
    n = new

print(n)

