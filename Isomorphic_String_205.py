# s = "egg"
# t = "add"

# s = "foo"
# t = "bar"

# s = "paper"
# t = "title"

s = "badc"
t = "baba"

dictS = {}
dictT = {}

def isSomorphic(self, s: str, t: str) -> bool:
    for i in range(len(s)):
        if s[i] in dictS and dictS[s[i]] != t[i]:
            return False
        if t[i] in dictS and dictT[t[i]] != s[i]:
            return False
        
        dictS[s[i]] = t[i]
        dictT[t[i]] = s[i]
    return True

def isSomorphic(self, s: str, t: str) -> bool:
    return [s.find(i) for i in s] == [t.find(i) for i in t]

def isSomorphic(self, s: str, t: str) -> bool:
    return map(s.find, s) == map(t.find, t)