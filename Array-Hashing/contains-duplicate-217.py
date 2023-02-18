'''
return true if any value appears at least twice in the array
return false if every element is distinct.
nums = [1,2,3,1] -> true
nums = [1,2,3,4] -> false
nums = [1,1,1,3,3,4,3,2,4,2] -> true
'''

def containsDuplicate(nums):
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


