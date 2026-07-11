class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)

        # Traverse from the last digit to the first

        for i in range(n - 1, -1, -1):

            # If digit is less than 9, just add 1 and return

            if digits[i] < 9:

                digits[i] += 1

                return digits

            # If digit is 9, make it 0 and continue

            digits[i] = 0

        # If we reach here, all digits were 9

        return [1] + digits