class Solution:
    def countBits(self, n: int) -> List[int]:
        response = []
        def count_one(n):
            print(n,"..n..")
            count = 0
            while n:
                n= n&(n-1)
                count+=1
            print(count)
            return count
        for i in range(n+1):
            res = count_one(i)
            response.append(res)
        return response