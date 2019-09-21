class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        index = len(digits) - 1
        while index >= 0:
            digits[index] += 1
            if digits[index] == 10:
                digits[index] = 0
                if index == 0:
                    digits.insert(0, 1)
                    break
                else:
                    index -= 1
            else:
                break
        return digits