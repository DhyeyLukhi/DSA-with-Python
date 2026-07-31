class Solution:
    def lengthOfLastWord(self, s):
        s = s[::-1]
        s = s.split(' ')
        i= 0
        while True:
            if s[i]:
                return len(s[i])

            else:
                i+=1



test = Solution()
ans = test.lengthOfLastWord(s="   fly me   to   the moon  ")
print(ans)