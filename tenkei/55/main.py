n, p, q  = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for i1 in range(n-4):
    product1 = a[i1]%p
    for i2 in range(i1+1,n-3):
        product2 = product1*a[i2]%p
        for i3 in range(i2+1,n-2):
            product3 = product2*a[i3]%p
            for i4 in range(i3+1,n-1):
                product4 = product3*a[i4]%p
                for i5 in range(i4+1,n):
                    product5 = product4*a[i5]%p
                    if product5 ==q :
                        cnt +=1
print(cnt)