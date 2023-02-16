# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

nums = [3,2,3]
target = 6

newList = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            newList.append(i)
            newList.append(j)
    

# for i, j in enumerate(nums[:-1]):
#     if j + nums[i] == target:
#         newList.append(i)
#         newList.append(i+1)
    
print(newList)