class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sample_str = ''
        for val in digits:
            sample_str=sample_str+str(val)
        sample_result = int(sample_str) + 1
        sample_result  = list(map(int, list(str(sample_result))))
        return sample_result 
