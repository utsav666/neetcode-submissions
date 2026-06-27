class Solution:
    def isHappy(self, n: int) -> bool:
        sum_collection = set()
        def sumup(n):
            sum_sq = 0
            while n > 0:
                r = n%10
                sum_sq = sum_sq + (r**2)
                n=n//10
            return sum_sq
        while n != 1:
            if n in sum_collection:
                return False
            sum_collection.add(n)
            n = sumup(n)
        return True
        
        