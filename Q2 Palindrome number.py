class Solution:
    def __init__(self):
        pass

    def isPalindrome(self, x):
        palin = 0
        check = x
        while x > 0:
            palin*=10
            palin += int(x%10)
            x = int(x/10)
        return palin==check



test = Solution()
print(test.isPalindrome(x=int(input())))