class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hm = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c not in hm:
                stack.append(c)
            else:
                if stack and stack[-1] == hm[c]:
                    stack.pop()
                else:
                    return False

        return not stack
                    
