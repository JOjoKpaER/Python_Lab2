s = input()
if len(s) % 2 == 0:
    s1 = s[(len(s) // 2 - 1):0:-1] + s[0]
    s2 = s[(len(s) // 2):-1] + s[-1]
    for i in range(len(s)//2):
        for j in range(len(s)//2 - i):
            print(" ", end='')
        print(s1[i], end='')
        for j in range(i*2):
            print(" ", end='')
        print(s2[i], end='')
        print()
else:
    s1 = s[(len(s) // 2 - 1):0:-1] + s[0]
    s2 = s[(len(s) // 2 + 1):-1] + s[-1]
    s3 = s[(len(s) // 2)]
    for j in range(len(s)//2 + 1):
        print(" ", end='')
    print(s3)
    for i in range(0, len(s)//2):
        for j in range(len(s)//2 - i):
            print(" ", end='')
        print(s1[i], end='')
        for j in range(i*2 + 1):
            print(" ", end='')
        print(s2[i], end='')
        print()
