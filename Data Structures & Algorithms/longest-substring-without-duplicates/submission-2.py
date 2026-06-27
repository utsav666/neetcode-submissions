class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =0
        max_len=0
        char_holder = set()
        for right in range(len(s)):
            while s[right] in char_holder:
                char_holder.remove(s[left])
                left=left+1
            char_holder.add(s[right])
            max_len=max(max_len, right-left+1)
        return max_len