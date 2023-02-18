#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sol 1
        repeat = {}
        count = 0
        for i in nums:
            if i in repeat:
                count += repeat[i]
                repeat[i] += 1
            else:
                repeat[i] = 1
        if count > 0:
            return True
        return False

        # Sol 2
        setNum = set()
        for i in nums:
            if i in setNum:
                return True
            setNum.add(i)
        return False
        
        # Sol 3
        repeat = {}
        for i in range(len(nums)):
            if repeat.get(nums[i]):
                return True
            repeat[nums[i]] += 1
        return False
        
        # Sol 4
        repeat = {}
        for i in range(len(nums)):
            repeat[nums[i]] = repeat.get(nums[i], 0) + 1
            if repeat.get(nums[i], 0) > 1:
                return True
        return False
# @lc code=end

