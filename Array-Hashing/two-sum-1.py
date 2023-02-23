def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {} # val: index

    for right, left in enumerate(nums): # get the index of dict
        remain = target - left # right
        if remain in seen: # this is right
            return [seen[remain], right] # return value of right
        seen[left] = right
    return