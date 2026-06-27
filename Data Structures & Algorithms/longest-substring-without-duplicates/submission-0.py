class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        seen = set()
        sample_set ={}
        max_len =0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[l])
                l=l+1
            seen.add(s[right])
            max_len = max(max_len,right-l+1)
        return max_len
            