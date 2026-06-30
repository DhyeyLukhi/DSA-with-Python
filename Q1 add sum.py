class Solution:
    def __init__(self):
        None

    def twoSum(self, nums: list[int], target: int):
        seen = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return seen[complement], index
            seen[value] = index

        return None



objs = Solution()
print(objs.twoSum(nums=[3, 2, 4], target=6))