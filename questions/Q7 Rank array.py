class Solution:
    def arrayRankTransform(self, arr):
        rank = 0
        min = arr[0]
        for i in range(0, len(arr)):
            for j in range(1, len(arr)):
                pass


test = Solution()
ans = test.arrayRankTransform([37,12,28,9,100,56,80,5,12])
print(ans)