class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        var = len(nums)
        for v,i in enumerate(nums):
            var =var^v^i
        return var