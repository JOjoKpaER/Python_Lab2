lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if len(lst) % 2 == 0:
    for i in range(0, len(lst), 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
else:
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)
