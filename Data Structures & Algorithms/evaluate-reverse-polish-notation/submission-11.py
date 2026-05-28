class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hm = {"+": "1", "-": "2", "*": "3", "/": "4"}
        stack = []

        for token in tokens:
            if not token in hm:
                stack.append(int(token))
            else:
                if hm[token] == "1":
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif hm[token] == "2":
                    second = int(stack.pop())
                    first = int(stack.pop())
                    stack.append(first - second)
                elif hm[token] == "3":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                else:
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(float(first) / second))
        
        return int(stack[-1]) if stack else 0