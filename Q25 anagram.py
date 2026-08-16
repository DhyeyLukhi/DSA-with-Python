class Solution:
    def isAnagram(self, s, t) -> bool:
        if s and not t or t and not s:
            return False
        words = {}
        for i in range(0, len(s)):
            if s[i] in words:
                words[s[i]]+=1

            else:
                words[s[i]] = 1

        for i in range(0, len(t)):
            if t[i] in words:
                words[s[i]]-=1

test = Solution()
ans = test.isAnagram(s="anagram", t="gramana")
print(ans)