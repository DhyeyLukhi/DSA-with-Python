class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            print(haystack.index(needle))
        
        else:
            return -1


test = Solution()
test.strStr(haystack="sadbutsad", needle="sad")