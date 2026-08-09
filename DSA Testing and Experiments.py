l1=[2,2,1,1,1,2,2]
l2 = l1[0]
for _ in range(0, len(l1)):
    if l2[0] == l1[_]:
        l2[_] = l1[_]
        l1.pop()

l1.remove()