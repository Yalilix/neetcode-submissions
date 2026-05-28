class Solution:
    def isValid(self, s: str) -> bool:
        hash = {']': '[', ')': '(', '}': '{'}
        stack = []
        for c in s:
            if c in hash and stack:
                char = stack.pop()
                if char != hash[c]:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
