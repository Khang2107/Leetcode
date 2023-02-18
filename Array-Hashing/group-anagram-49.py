def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    '''
    # Sol 1
    ans = {}
    for word in strs:
        temp = ''.join(sorted(word))
        print(temp)
        if temp not in ans:
            ans[temp] = []
        
        ans[temp].append(word)
    return list(ans.values())
    '''
    
    '''
    # Sol 2
    ans = {}
    for word in strs:
        temp = ''.join(sorted(word))
        print(temp)
        if temp in ans:
            ans[temp].append(word)
        else:
            ans[temp] = [word]
        print(ans)
    return ans.values()
    '''
    

    