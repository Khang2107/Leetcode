'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Eg1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Eg2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
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
            
