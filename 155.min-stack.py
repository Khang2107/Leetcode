#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
class minStack(object):
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # check if minStack is empty
        # if minStack is not empty, compare current val with most recent added
        if self.minStack:
            val = min(self.minStack[-1], val)
        # if empty, assign val
        else:
            val = val
        self.minStack.append(val)
    
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        # return most recent stack
        return self.stack[-1]
    
    def getMin(self):
        """
        :rtype: int
        """
        # return smallest val = top of minStack
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
