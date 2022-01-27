s = input()
p, q = map(int,input().split())
a, b = p-1, q-1
A = s[a]
B = s[b]
ans = s[:a] + B +s[a+1:b] + A + s[b+1:len(s)]
print(ans)

