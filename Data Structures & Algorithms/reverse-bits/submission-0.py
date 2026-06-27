class Solution:
    def reverseBits(self, n: int) -> int:
        print(n, "input")

        n &= (1 << 32) - 1   # same as your uN mask
        print(n, "masked_32")

        rev = 0
        for _ in range(32):
            rev = (rev << 1) | (n & 1)
            n >>= 1

        print(rev, "reversed_int")
        return rev