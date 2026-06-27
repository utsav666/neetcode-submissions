import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sample_ans = []
        final_ans = []
        for val in points:
            dist = sqrt((val[0]-0)**2 +(val[1]-0)**2)
            sample_ans.append([dist,val])
        sample_ans = sorted(sample_ans)
        for v in range(k):
            final_ans.append(sample_ans[v][1])
        return final_ans
            