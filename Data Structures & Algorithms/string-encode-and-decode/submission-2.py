class Solution:

    def encode(self, strs: List[str]) -> str:
        sample_temp = ""
        for val in strs:
            if "#" in val:
                val.replace("#",'*')
            sample_temp = sample_temp+str(len(val))+"#"+val
        return sample_temp
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            j = i
            
            # read number until '#'
            while s[j] != '#':
                j += 1

            length = int(s[i:j])  # full length (may be multiple digits)
            start = j + 1
            end = start + length

            result.append(s[start:end])
            i = end  # move pointer
        
        return result