# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))

        return stack[-1]
