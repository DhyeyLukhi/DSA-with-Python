class Solution:
    def majorityElement(self, nums):
        major = nums[0]
        before = len(nums)
        try:
            for i in range(len(nums)):
                if major == nums[i]:
                    nums.remove(nums[i])

        except Exception as e:
            pass

        finally:
            print(major, nums)

test = Solution()
ans = test.majorityElement(nums=[2,2,1,1,1,2,2,2])
print(f"Answer is {ans}")