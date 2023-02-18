#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            temp = ''.join(sorted(word))
            print(temp)
            if temp in ans:
                ans[temp].append(word)
            else:
                ans[temp] = [word]
            print(ans)
        return ans.values()
        
# @lc code=end

