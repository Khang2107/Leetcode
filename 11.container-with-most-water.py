#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        
        while left < right:
            wide = right - left # calculate width of the box
            high = min(height[left], height[right]) # calculate the possible height by taking lower bar
            maxArea = max(maxArea, wide*high) # compare the maxarea with the previous one and taking whichever is higher

            if height[left] < height[right]: # move left pointer if the left bar is shorter
                left += 1
            else: # move right pointer if the right bar is shorter
                right -= 1
        return maxArea
        
# @lc code=end
