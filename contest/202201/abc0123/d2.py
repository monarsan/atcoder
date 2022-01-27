from itertools import  permutations
n = int(input())
a = [[0]*(2*n-1)]*(2*n-1)

for i in range(2*n-1):
    a[i] = list(map(int, input().split()))
ans = 0
def func(list, acc):
    for p in permutations(list, 2):
        p = list(p)
        x = a[min(p[i], p[i])][max(p[i], p[i]) -1 - min(p[i], p[i])]
        acc = x^acc
        ans = max(ans, acc)
        new_list = [i for i in list if i not in p]
        func(new_list, acc)

func(range(2*n), 0)
print(ans)


