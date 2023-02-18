'''
return true if t is anagram of s, false if not
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

s = "anagram", t = "nagaram" -> true
s = "rat", t = "car" -> false
'''

def isAnagram(self, s: str, t: str) -> bool:
    '''
    # Sol 1
    if len(s) != len(t):
        return False
    
    dictS, dictT = {}, {}
    for i in range(len(s)):
        dictS[s[i]] = dictS.get(s[i], 0) + 1
        dictT[t[i]] = dictT.get(t[i], 0) + 1
    return dictS == dictT
    '''
    
    '''
    # Sol 2
    if len(s) != len(t):
        return False
    
    dictS, dictT = {}, {}
    for i in s:
        dictS[i] = dictS.get(i, 0) + 1
    for i in t:
        dictT[i] = dictT.get(i, 0) + 1
    return dictS == dictT
    '''
    
    '''
    # Sol 3
    return sorted(s) == sorted(t)
    '''
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    for j in t:
        if j in dict:
            dict[j] -= 1 # avoid having to scan through it again - duplicate, aim to make dict empty
        else:
            return False
    
    for val in dict.values():
        if val != 0: # if dict is not empty: different set
            return False
    return True