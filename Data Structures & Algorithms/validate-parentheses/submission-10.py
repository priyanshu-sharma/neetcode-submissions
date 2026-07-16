class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif len(stack) > 0:
                if i == ')' and stack[-1] == '(' or i == ']' and stack[len(stack) - 1] == '[' or i == '}' and stack[len(stack) - 1] == '{':
                    stack.pop(len(stack) - 1)
                else:
                    return False
            else:
                return False
        return len(stack) == 0