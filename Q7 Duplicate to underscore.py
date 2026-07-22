class Solution:
    def removeDuplicates(self, nums):
        nums = list(nums)
        last = 0
        
        for i in range(1, len(nums)):
            if nums[last] == nums[i]:
                nums[i] = "_"

            else:
                last+=1
                nums[last], nums[i] = nums[i], nums[last]
        
        return last+1, nums

test = Solution()
ans, lst = test.removeDuplicates([1,1,2])
print(ans, lst)