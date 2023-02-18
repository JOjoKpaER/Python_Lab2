lst = input().lower().split(sep=' ')
nums = input().split()
print(lst[int(nums[0])-1].capitalize(), end=' ')
for i in nums[1:]:
    print(lst[int(i)-1], end=' ')
