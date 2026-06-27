import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sample_data = []
        for val in nums:
            heapq.heappush(sample_data,val)
        while len(sample_data) != k:
            heapq.heappop(sample_data)
        return sample_data[0]