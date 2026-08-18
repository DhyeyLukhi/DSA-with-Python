class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
            
        # Phase 2: Verify candidate
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        
test = Solution()
ans = test.majorityElement(nums=[6,5,5])
print(f"Answer is {ans}")