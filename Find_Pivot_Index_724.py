from operator import truediv


# nums = [1,7,3,6,5,6]
# # nums = [2,1,-1]

# total = sum(nums)
# leftSum = 0
# for i in range(len(nums)):
#     rightSum = total - leftSum - nums[i]
#     if leftSum == rightSum:
#         print(i)
#     leftSum += nums[i]
    

def pivotIndex(nums):
    total = sum(nums)
    leftSum = 0
    for i in range(len(nums)):
        rightSum = total - leftSum - nums[i]
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1


# nums = [1,7,3,6,5,6]
nums = [2,1,-1]
nums = [1,2,3]
print(pivotIndex(nums))