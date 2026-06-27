class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = list(str(bin(n)[2:].zfill(32))).count('1')
        return res
        
        