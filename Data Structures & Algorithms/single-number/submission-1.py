#from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        var=0
        for v in nums:
            var=var^v
        return var