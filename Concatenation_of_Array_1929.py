# My Solution
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newList = []
        for i in nums:
            newList.append(i)
        
        for i in nums:
            newList.append(i)
        
        return newList
    

# Another Solution
# class Solution(object):
#     def getConcatenation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         return nums*2