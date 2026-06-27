import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # def calculation(stones):
        #     stones = sorted(stones ,reverse=True)
        #     f = stones.pop(0)
        #     s =  stones.pop(0)
        #     if f!=s:
        #         stones.append(f-s)
        #     return stones
        # while len(stones) > 1:
        #     stones = calculation(stones)
        # if len(stones) == 1:
        #     return stones[0]
        # else:
        #     return 0
        sample_list =stones
        sample_list = [-x for x in sample_list]
        heapq.heapify(sample_list)
        def calculate(sample_list):
            print(sample_list)
            x=heapq.heappop(sample_list)
            x=-1*x
            y=heapq.heappop(sample_list)
            y=-1*y
            if x != y:
                heapq.heappush(sample_list,(x-y)*-1)
            return sample_list
        while len(sample_list)!=1:
            if len(sample_list) ==0:
                return 0
            else:
                calculate(sample_list)
            
        if len(sample_list)==1:
            return sample_list[0]*-1
        else:
            return 0