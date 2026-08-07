class Solution:
    def generate(self, numRows):
        pascl = [[1]]
        newpasc = []
        for i in range(1, numRows):
                for j in range(0, len(pascl)+1):
                    if j == 0:
                        newpasc.clear()
                        newpasc.append(1)
        
                    elif j == len(pascl):
                        newpasc.append(1)
                        pascl.append(newpasc[:])
        
                    else:
                        sum = pascl[-1][j] + pascl[-1][j-1]
                        newpasc.append(sum)
        return pascl
        


test = Solution()
ans = test.generate(numRows=5)
print(ans)
