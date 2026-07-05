class Solution:
    def longestCommonPrefix(self, strs):
        pref = str(strs[0]) if strs else ""
        for i in range(0, len(pref)):
            for j in range(1, len(strs)):
                try:
                    if pref[i] == strs[j][i]:
                        pass
                    
                    else:
                        pref = pref.removesuffix(pref[i:])
                        return pref if pref else ""
                    
                except Exception as e:
                    pref = pref.removesuffix(pref[i:])
                    return pref if pref else ""
        return pref

test = Solution()
find = ["ab", "a"]
print(test.longestCommonPrefix(find))
