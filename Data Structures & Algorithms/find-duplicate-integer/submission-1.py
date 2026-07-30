from collections import Counter
# class ListNode:
#     def __init__(self,val=0):
#         self.val=val
#         self.next = None

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sample_freq = Counter(nums)
        return max(sample_freq, key=sample_freq.get)
        