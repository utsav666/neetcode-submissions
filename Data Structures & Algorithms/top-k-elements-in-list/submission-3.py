from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sample_freq = dict(Counter(nums))
        count =0
        ans = []
        final_res =[]
        for key,v in sample_freq.items():
            #if len(ans) > k:
            heapq.heappush(ans,(-v,key))
        print(ans)
        for i in range(k):
            count,key = heapq.heappop(ans)
            final_res.append(key)
        return final_res