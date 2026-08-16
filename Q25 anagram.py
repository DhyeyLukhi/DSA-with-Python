class Solution:
    def isAnagram(self, s, t) -> bool:
        if s and not t or t and not s:
            return False
        s = list(s)
        t = list(t)
        for i in range(0, len(s)):
            if s[i] in t:
                t.remove(s[i])

            else:
                return False
        
        return True if not t else False
                    
test = Solution()
ans = test.isAnagram(s="anagram", t="gramana")
print(ans)