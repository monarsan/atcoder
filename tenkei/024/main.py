n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += abs(a[i]-b[i])

if (sum <=k) & (sum%2 == k%2) :
    print("Yes")
else:
    print("No")