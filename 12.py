lst = [1, 2, 3, 1, 2, 4, 4, 5, 6, 6, 7]
for i in lst:
    if lst.count(i) < 2:
        print(i)
