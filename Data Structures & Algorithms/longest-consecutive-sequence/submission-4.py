class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        long=0
        length=0
        num_set =set(nums)
        sample_ans = []
        for num in num_set:
            if num-1 not in num_set:
                length =1
                curr = num
                while curr+1 in num_set:
                    #sample_ans.append(curr)
                    curr = curr+1
                    length = length+1
                long = max(length,long)
        return long