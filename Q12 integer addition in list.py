class Solution:
    def plusOne(digits):
        if digits[-1] == 9:
            digits.reverse()
            for i in range(0, len(digits)):
                if i == len(digits)-1:
                    if digits[i] == 9:
                        digits[i] = 0
                        digits.append(1)
                        digits.reverse()
                        break

                    else:
                            digits[i] = digits[i]+1
                            digits.reverse()
                            break

                elif digits[i] == 9:
                    digits[i] = 0
                
                else:
                    print("added")
                    digits[i] = digits[i]+1
                    digits.reverse()
                    break
        else:
            digits[-1] = digits[-1]+1

        return digits

test = Solution
ans = test.plusOne(digits=[9,9,9,9,9])
print(ans)