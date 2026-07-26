class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            sample_val = int(str(x)[::-1])
        else:
            pos = x*-1
            sample_val = int(str(pos)[::-1])*-1
        if -(2 ** 31) <= sample_val <= (2 ** 31 - 1):
            return sample_val
        else:
            return 0