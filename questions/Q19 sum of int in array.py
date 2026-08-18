class Solution:
    def __init__(self):
        None

    def twoSum(self, nums: list[int], target: int):
        seen = {}

        for index, value in enumerate(nums):
            remain = target - value
            if remain in seen:
                return seen[remain], index
            seen[value] = index

        return None



objs = Solution()
print(objs.twoSum(nums=[3, 2, 4], target=6))