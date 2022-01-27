n = int(input())

set = set()
l =[]
for i in range(n):
    s = input()
    if s not in set :
        set.add(s)
        print(i+1)