import regex as re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip()
        text = "".join(s.split())
        text=text.lower()
        cleaned = re.sub(r'[^A-Za-z0-9 ]', '', text)
        if cleaned == cleaned[::-1]:
            return True
        return False