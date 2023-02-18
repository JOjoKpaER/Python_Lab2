from itertools import groupby

s = input().lower()
groups = groupby(s)
result = [(label, sum(1 for _ in group)) for label, group in groups]
symb = str(result.__getitem__(0))[2]
shift = 0
for i in result:
    arrow = str(i)[2]
    n = int(str(i)[-2])
    if arrow == ">":
        for j in range(shift):
            print(" ", sep='', end='')
        for j in range(n):
            print(symb, sep='', end='')
            shift += 1
        print(" ")
    elif arrow == "<":
        for j in range(shift - n):
            print(" ", sep='', end='')
        for j in range(n):
            if shift <= 0:
                break
            print(symb, sep='', end='')
            shift -= 1
        print(" ")
    elif arrow.upper() == "V":
        for j in range(n):
            for k in range(shift):
                print(" ", sep='', end='')
            print(symb)
