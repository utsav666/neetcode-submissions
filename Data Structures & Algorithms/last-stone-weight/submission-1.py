class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def calculation(stones):
            stones = sorted(stones ,reverse=True)
            f = stones.pop(0)
            s =  stones.pop(0)
            if f!=s:
                stones.append(f-s)
            return stones
        while len(stones) > 1:
            stones = calculation(stones)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0