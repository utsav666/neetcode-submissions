class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper  = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in mapper:
                if not stack or mapper[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack

        