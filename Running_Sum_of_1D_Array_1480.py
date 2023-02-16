# def runningSum(self, nums):
#     newList = []
#     total = 0
#     for i in nums:
#         total += nums[i]
#         print(total)
#         i += 1




testList = [1,2,3,4]
total = 0
newList = []

for i in testList:
    total += i
    print(total)
    newList.append(total)
    
print(newList)