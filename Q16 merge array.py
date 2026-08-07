class Solution:
    def merge(self, nums1, m, nums2, n):
        if m == 0:
            nums1[:] = nums2
            return
        if n == 0:
            return
        # Ignore the trailing zeroes
        nums1[:] = nums1[:m]
        i = 0
        while i < len(nums1) and nums2:
            if nums1[i] <= nums2[0]:
                i += 1
            else:
                nums1.insert(i, nums2.pop(0))
                i += 1
        # If nums2 still has elements left
        nums1.extend(nums2)


test = Solution()
ans = test.merge(nums1=[4,0,0,0,0,0],  m=1, nums2=[1,2,3,5,6], n=5)
        