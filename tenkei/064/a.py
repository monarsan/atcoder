n, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    ans += abs(a[i]-a[i+1])
for i in range(q):
    l, r, v = map(int, input().split())
    if l == 1 & r == n:
        ans = ans
    elif l == 1 :
        ans += abs(v+a[r-1] - a[r])
    elif r == n:
        ans += abs(a[l-1] - a[l]-v)
    else:
        ans += abs(v+a[r-1] - a[r]) + abs(a[l-1] - a[l]-v)
    print(ans)
