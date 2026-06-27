class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i , v in enumerate(nums):
            sample_val = target-v
            if sample_val in hash_map :
                return [hash_map[sample_val],i]
            hash_map[v]=i
  