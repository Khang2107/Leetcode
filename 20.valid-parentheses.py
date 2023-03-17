#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in s:
            if i == "{":
                stack.append("}")
            elif i == "[":
                stack.append("]")
            elif i == "(":
                stack.append(")")
            elif not stack or stack.pop() != i:
                return False
        return not stack
        
# @lc code=end

