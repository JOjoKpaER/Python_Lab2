lst = [1, -2, 3, 4, -5, 6, -7, -8, 9]
prev = lst[0]
for i in lst[1:-1]:
    if int(prev) * int(i) > 0:
        print(prev, i)
        break
    else:
        prev = i

