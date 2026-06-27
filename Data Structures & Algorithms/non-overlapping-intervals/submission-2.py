class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prev=intervals[0][1]
        remove=0
        for s,e in intervals[1:]:
            if s<prev:
                remove+=1
            else:
                prev=e
        return remove
