n, m = map(int, input().split())
s = list(input().split())
t = set(input().split())
for i in s:
    if i in t:
        print("Yes")
    else :
        print("No")