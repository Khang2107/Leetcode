def pivotIndex(self, nums: List[int]) -> int:
    leftSum = 0
    total = sum(nums)
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        if leftSum == rightSum:
            return nums[i]
        else:
            leftSum += nums[i]
    return -1