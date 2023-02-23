def twoSum(self, nums: List[int], target: int) -> List[int]:
    '''
    # Sol 1:
    seen = {} # val: index

    for right, left in enumerate(nums): # get the index of dict
        remain = target - left # right
        if remain in seen: # this is right
            return [seen[remain], right] # return value of right
        seen[left] = right
    return
    '''

    '''
    # Sol 2:
    ans = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                ans.append(i)
                ans.append(j)
    return ans
    '''