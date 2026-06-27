from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sample_dict = dict(Counter(nums))
        for val in sample_dict.keys():
            if sample_dict[val] > 1:
                return val
