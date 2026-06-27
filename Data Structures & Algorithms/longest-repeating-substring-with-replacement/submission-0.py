class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        best=0
        freq_dict = {}
        max_freq = 0
        for right in range(len(s)):
            freq_dict[s[right]] = freq_dict.get(s[right],0)+1
            max_freq = max(max_freq,freq_dict[s[right]])
            while (right-l+1) - max_freq > k:
                freq_dict[s[l]]-=1
                l=l+1
            best = max(best,right-l+1)
        return best