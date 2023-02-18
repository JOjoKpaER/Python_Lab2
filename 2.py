s1 = input()
s2 = s1[((len(s1)+1)//2):-1] + s1[-1] + s1[0:((len(s1)+1)//2)]
print(s2)
