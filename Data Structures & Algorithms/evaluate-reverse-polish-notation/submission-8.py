class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashmap = {'+', '-', '*', '/'}
        stack = []

        for tok in tokens:
            if tok in hashmap:
                summ = 0
                if tok == '+':
                    summ = stack.pop() + stack.pop()
                elif tok == '-':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    summ = num2 - num1 
                elif tok == '*':
                    summ = stack.pop() * stack.pop()
                elif tok == '/':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    summ = int(float(num2) / num1)
                stack.append(summ)
            else:
                stack.append(int(tok))
        return stack[0]