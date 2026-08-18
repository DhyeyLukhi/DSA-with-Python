import time


class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        if n == 0:
            return ans

        else:
            ans = 1
            prev = 1
            for i in range(0, n-1):
                ans += prev
                prev = ans-prev


        return ans



test = Solution()
start = time.perf_counter()
ans = test.climbStairs(n=4)
end = time.perf_counter()
print(ans)
print(f"Time taken {(end-start)*1000:.6f} ms")
