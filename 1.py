s = input()
if len(s) > 2:
    print(s[2])             # 1
if len(s) > 1:
    print(s[-2])            # 2
if len(s) > 4:
    print(s[:4])           # 3
if len(s) > 2:
    print(s[:-2])          # 4
print(s[::2])              # 5
if len(s) > 0:
    print(s[1:-1:2])        # 6
print(s[::-1])              # 7
if len(s) > 0:
    print(s[::-2])        # 8
print(len(s))               # 9


