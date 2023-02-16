from ast import List

# Sol 1 - time: 0:0:42
def getConcatenation(self, nums: List[int]) -> List[int]:
    return nums * 2

# Sol 2 - 0:03:16
def getConcatenation(self, nums: List[int]) -> List[int]:
    res = []
    for i in nums:
        res.append(i)
    for i in nums:
        res.append(i)
    return res

# Sol