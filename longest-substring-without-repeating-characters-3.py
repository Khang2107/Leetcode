# Sol 1 - using dictionary
def lengthOfLongestSubstring(self, s: str) -> int:
    res = 0
    slow = 0
    seen = {}
    
    for fast in range(len(s)):
        if s[fast] in seen and slow <= seen[s[fast]]:
            slow = seen[s[fast]] + 1
        else:
            res = max(res, fast - slow + 1)
        seen[s[fast]] = fast
    return res


# Sol 2 - using set
def lengthOfLongestSubstring(self, s: str) -> int:
    seen = set()
    res = 0
    slow = 0
    
    for fast in range(len(s)):
        while s[fast] in seen:
            seen.remove(s[slow])
            slow += 1
        
        seen.add(s[fast])
        res = max(res, fast - slow + 1)
    return res