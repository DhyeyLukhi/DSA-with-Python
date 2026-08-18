import time


class Solution:
    def mySqrt(self, x):
        right = x
        left = 0
        mid = (right-left)//2
        while left <= right:
            if mid*mid == x:
                return mid

            elif mid*mid < x and (mid+1)*(mid+1) >= x:
                return mid+1 if (mid+1)*(mid+1) == x else mid

            elif mid*mid < x:
                left = mid+1
                mid = (left+right)//2

            elif mid*mid > x:
                right = mid-1
                mid = (left+right)//2

test = Solution()
start = time.perf_counter()
ans = test.mySqrt(x=8)
end = time.perf_counter()

print(ans)
print(f"Execution time: {(end-start)*1000:.6f} ms")
