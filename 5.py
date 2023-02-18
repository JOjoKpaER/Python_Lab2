s = input()
t = s[0]
while True:
    s = input()
    if len(s) > 0:
        if t != s[0]:
            break
    else:
        break
print(s)
