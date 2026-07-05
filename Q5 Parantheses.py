class Solution:
    def isValid(self, paran):
        braces = []
        for i in range(0, len(paran)):
            if paran[i] == '(' or paran[i] == '{' or paran[i] == '[':
                braces.append(paran[i])
            else:
                if braces:
                    last_entry = braces.pop(-1)
                else:
                    return False
                if paran[i] == ')' and last_entry == '(':
                    continue
                elif paran[i] == '}' and last_entry == '{':
                    continue
                elif paran[i] == ']' and last_entry == '[':
                    continue
                else:
                    return False
        return False if len(braces) else True
 

test = Solution()
print(test.isValid(r"()({}"))