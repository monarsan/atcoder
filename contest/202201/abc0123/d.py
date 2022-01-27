from itertools import  permutations
n = int(input())
a = [[0]*(2*n-1)]*(2*n-1)

for i in range(2*n-1):
    a[i] = list(map(int, input().split()))
ans = 0
for comb1 in permutations(range(2*n),n):
    comb2 = [i for i in range(2*n) if i not in comb1]
    x0 = 0
    for i in range(n):
        
        x = a[min(comb1[i], comb2[i])][max(comb1[i], comb2[i]) -1 - min(comb1[i], comb2[i])]
        x0 = x0^x

    ans = max(ans, x0)
print(ans)

