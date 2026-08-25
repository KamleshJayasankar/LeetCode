class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num += 1 << 32

        hex_digits = "0123456789abcdef"
        result = []

        while num > 0:
            result.append(hex_digits[num & 0xF])
            num >>= 4

        return "".join(reversed(result))