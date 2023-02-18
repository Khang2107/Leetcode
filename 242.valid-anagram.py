#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        for j in t:
            if j in dict:
                dict[j] -= 1 # avoid having to scan through it again - duplicate, aim to make dict empty
            else:
                return False
        
        for val in dict.values():
            if val != 0: # if dict is not empty: different set
                return False
        return True
        
# @lc code=end

