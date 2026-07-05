# class Solution:
#     def romanToInt(self, roman):
#         symb = {'I':1, 
#                      'V':5, 
#                      'X':10, 
#                      'L':50, 
#                      'C':100, 
#                      'D':500, 
#                      'M':1000}
#         special = {'IV': 4,
#                    'IX':9,
#                    'XL':40,
#                    'XC':90,
#                    'CD':400,
#                    'CM':900}
#         max = 'I'
#         ans = 0
#         for i in range(0, len(roman)):
#             if symb[roman[i]] > symb[max]:
#                 max = roman[i]
        
#         for i in range(0, len(special)):
#             if list(special.keys())[i] in roman:
#                 ans+=special[list(special.keys())[i]]
#                 roman = str(roman).replace(list(special.keys())[i], "")
        
#         for i in range(0, len(roman)):
#             ans+=symb[roman[i]]
        
#         print(ans)


# test = Solution()
# test.romanToInt("MCMXCIV")


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        total = 0

        for i in range(len(s)):
            if i+1 <len(s) and roman[s[i]] < roman[s[1+i]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total
        
test = Solution()
print(test.romanToInt("MCMXCIV"))