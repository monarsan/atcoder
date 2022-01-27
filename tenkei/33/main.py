h, w = map(int, input().split())
print((h+1)//2 * ((w+1)//2))

if (h%2 == 0) &(w%2 == 0):
    print((h/2) *(w/2))
elif (h%2 == 0) &(w%2 == 1):
    print((h/2) *((w+1)/2))
elif (h%2 == 0) &(w%2 == 1):
    print((w/2) *((h+1)/2))
else:
    print((w/2) *((h+1)/2))