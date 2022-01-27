n, q = map(int, input().split())
a = list(map(int, input().split()))
def add01(x):
    return x + 0.1
b = map(add01, a)
c = [0]*(n-1)
for i in range(n-1):
    if a[i]*a[i+1] >0:
        c[i] = 0
    else:
        c[i] = 1

ans = 0
for i in range(n-1):
    ans += abs(a[i]-a[i+1])
print("ans0" + ans)
for i in range(q):
    l, r, v = map(int, input().split())
    if(l ==r):
        ans += 2*v
    elif l == 1 & r == n:
        num = sum(c[l-1:r-1])
        ans = v * num
    elif l == 1 | r == n:
        num = sum(c[l-1:r-1])
        ans += v+(1+num)
    else:
        num = sum(c[l-1:r-1])
        ans += v *(2 + num)
    print(ans)
