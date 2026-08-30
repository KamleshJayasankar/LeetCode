class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        total = 10
        unique_digits = 9
        available_choices = 9

        for i in range(2, n + 1):
            unique_digits *= available_choices
            total += unique_digits
            available_choices -= 1

        return total