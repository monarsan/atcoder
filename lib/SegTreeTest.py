import SegTree

list1 = [1,2,3,4]
list2 = [43, 32,54,13,564]

def max2(a, b):
    return max(a,b)

seg1 = SegTree(list1, max, -9999999)
print(seg1.max(0,2) == 2)
print(seg1.max(0,4) == 4)

seg2 = SegTree(list2, max, -9999999)
print(seg1.max(0,2) == 43)
print(seg1.max(0,4) == 564)