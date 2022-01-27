q = int(input())
top = []
btm =[]


for i in range(q):
    t, x = map(int,input().split())
    if t==1:
        top.append(x)
    elif t ==2:
        btm.append(x)
    else:
        if(x <= len(top)):
            print(top[len(top)-x])
        else:

            print(btm[x-len(top)-1])