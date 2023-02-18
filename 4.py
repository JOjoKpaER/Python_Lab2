s = input()
symb = "f"
if s.find(symb) != -1:
    if s.find(symb) == s.rfind(symb):
        print (s.find(symb))
    else:
        print (s.find(symb), s.rfind(symb))
