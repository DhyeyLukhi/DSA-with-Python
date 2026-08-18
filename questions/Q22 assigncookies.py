class Solution:
    def findContentChildren(self, g, s):
        child =0
        cookie=0
        # g is for child
        # s is for cookies
        while len(g) > 0:
            cookie=0
            while len(s) > 0:
                print(f"G:{g} \nS:{s} \ncookies:{cookie}")
                if g[0] <= s[cookie]:
                    print("Child got it")
                    child+=1
                    s.pop(cookie)
                    break

                elif g[0] > s[cookie]:
                    print("child dropped")
                    cookie+=1

                    if cookie > len(s)-1:
                        print("stay low child")
                        break
            print("child remved")
            g.pop(0)

            return child
            



test = Solution()
ans = test.findContentChildren(g=[1,2], s=[1,2,3])
print(ans)