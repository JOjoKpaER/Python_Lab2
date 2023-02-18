import random

lst = list()
for i in range(8):
    lst.append([random.randint(0, 7), random.randint(0, 7)])
chk = True
print(lst)
for i in lst:
    for j in lst:
        if i == j:
            continue
        if j[0] == i[0] or j[1] == i[1]:
            print("YES")
            chk = False
            break
    if not chk:
        break
if chk:
    print("NO")
