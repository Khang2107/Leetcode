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


# Sol 3 - dictionary
def lengthOfLongestSubstring(self, s: str) -> int:
    res = 0
    slow = 0
    seen = {}
    
    for fast in range(len(s)):
        # if s[fast] not in seen, keep increasing window size & move right
        if s[fast] not in seen:
            res = max(res, fast - slow + 1)
        # if s[fast] in seen, we have two cases:
        else:
            # case 1: s[fast] is inside the current window, change window by moving slow to seen[s[fast]] + 1
            # case 2: s[fast] is not inside the current window, increase window
            if seen[s[fast]] < slow:
                res = max(res, fast - slow + 1)
            else:
                slow = seen[s[fast]] + 1
        seen[s[fast]] = fast
    return res