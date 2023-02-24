'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

'''

# Explanation
'''
Here's a line-by-line explanation of the Python code:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

This defines a class called Solution with a method called threeSum. The method takes a list of integers called nums as input and returns a list of lists of integers.

nums.sort()
This sorts the input list of integers in ascending order. This is done so that we can easily compare elements in the list.

res = []
This creates an empty list called res which will be used to store the triplets that sum to zero.

for i in range(len(nums) - 2):
This starts a loop that iterates over the input list nums, up to the second last element. We use len(nums) - 2 as the upper limit because we need at least two more elements to the right of the current element i to form a triplet.

if i > 0 and nums[i] == nums[i-1]:
    continue
This skips the current iteration if the current element is equal to the previous element and the current element is not the first element. This is done to avoid duplicate triplets.

left, right = i+1, len(nums)-1
This initializes two pointers, left and right, which are used to find the other two elements that sum to zero with the current element nums[i]. left is initialized to i+1, which is the next element to the right of the current element. right is initialized to the last element in the list.

while left < right:
    total = nums[i] + nums[left] + nums[right]
This starts a loop that continues as long as left is less than right. This loop is used to move the left and right pointers towards the middle of the list to find other elements that can form a triplet. total is the sum of the current element nums[i], the element pointed to by left, and the element pointed to by right.

if total == 0:
    res.append([nums[i], nums[left], nums[right]])
    while left < right and nums[left] == nums[left+1]:
        left += 1
    while left < right and nums[right] == nums[right-1]:
        right -= 1
    left += 1
    right -= 1

If total is zero, then we have found a triplet that sums to zero. We add the triplet to the res list. We then move the left pointer to the next element to the right that is different from the current element, and move the right pointer to the next element to the left that is different from the current element. This is done to avoid duplicate triplets. Finally, we move both pointers towards the middle of the list to find other triplets that sum to zero.

elif total < 0:
    left += 1
If total is less than zero, then the sum can be increased by moving the left pointer towards the middle of the list. This is because the list is sorted in ascending order, so increasing the left pointer will increase the value of the sum.

else:
    right -= 1
If total is greater than zero, then the sum can be decreased by moving the right pointer towards the middle of the list. This is because the list is sorted in ascending order, so decreasing the right pointer will decrease the value of the sum.

return res
This returns the res list, which contains all the triplets that sum to zero in the input list nums.

Overall, this solution uses two pointers to find all possible triplets in the input list that sum to zero. By sorting the input list first, we can use the fact that the list is in ascending order to efficiently move the pointers towards the middle of the list to find triplets. The solution also handles duplicate elements in the list to avoid duplicate triplets in the result.
'''

def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort() # sort the array to find the triplets (3 numbers)
    res = [] 

    # run for loop up to the second last element
    # len(nums) - 2 used as upper limit because we need 2 more element to the right of i to form a triplet (list of 3 numbers)
    for i in range(len(nums) - 2):
        # skip current iteration if current element == previous and current is not the first element
        # avoid duplicate triplets
        if i > 0 and nums[i] == nums[i-1]:
            continue 
        
        # left is the item next to current i
        # right is the rightmost item
        left = i+1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else: 
                # if total = 0
                res.append([nums[i], nums[left], nums[right]])
                
                # we make sure left and right does not point to the same value as they did with previous i
                # avoid duplicate triplets
                # ensure that left points to new element different from previous one
                # after we find a triplet that sums to zero
                # we need to move the left pointer to next unique element
                # it is to check if current is a duplicate of next element in the list
                # If it is duplicate, we increment left by 1 to skip over the duplicate element and move to the next unique element in the list
                
                while left < right and nums[left] == nums[left+1]:
                    # this left += 1 is only to skip over the duplicates when nums[left] == nums[left+1]
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                    
                # after we update the pointers, we move left and right to the middle of the list
                # regardless of whether there is duplicates
                left += 1; right -= 1
        
    return res