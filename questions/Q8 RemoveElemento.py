class Solution:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums), nums


test = Solution()
list1 = [0,1,2,2,3,0,4,2]
k, items=test.removeElement(nums=[0,1,2,2,3,0,4,2], val=2)
print(k, items)
