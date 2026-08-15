class Solution:
    def findMaxConsecutiveOnes(self, nums):
        conse = 0
        count = 0
        for num in nums:
            if num == 1:
                conse+=1
                
            else:
                count = max(count, conse)
                conse = 0

        count = max(count, conse)
        return count


test = Solution()
ans = test.findMaxConsecutiveOnes(nums=[1,0,1,1,1,0,1])
print(f"Answer is {ans}")