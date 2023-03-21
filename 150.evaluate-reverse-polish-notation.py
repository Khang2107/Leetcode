#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                right = stack.pop()
                left = stack.pop()
                if i == "+":
                    stack.append(left + right)
                elif i == "*":
                    stack.append(left * right)
                elif i == "-":
                    stack.append(left - right)
                elif i == "/":
                    stack.append(int(float(left) / right))

        return stack.pop()

# @lc code=end
