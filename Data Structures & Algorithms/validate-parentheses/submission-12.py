class Solution:
    def isValid(self, s: str) -> bool:
        hm = {"}": "{", ")": "(", "]": "["}
        stack = []

        for c in s:
            if not c in hm:
                stack.append(c)
            else:
                if stack and stack.pop() == hm[c]:
                    continue
                else:
                    return False
        
        return True if not stack else False

            