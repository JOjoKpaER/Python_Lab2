import sys

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
prev = sys.maxsize
for i in lst:
    print("\n", i, "prev=", prev, ":")
    for j in lst:
        if prev < int(j):
            print(j, end=' ')
    prev = int(i)

