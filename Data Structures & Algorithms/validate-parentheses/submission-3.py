class Solution:
    def isValid(self, s: str) -> bool:
        data_stack = []
        for i in s:
            if i in ['(', '{', '[']:
                data_stack.append(i)
            elif len(data_stack) > 0 and i == ')' and data_stack[len(data_stack) - 1] == '(' or len(data_stack) > 0 and i == '}' and data_stack[len(data_stack) - 1] == '{' or len(data_stack) > 0 and i == ']' and data_stack[len(data_stack) - 1] == '[':
                data_stack.pop(len(data_stack) - 1)
            else:
                return False
        if len(data_stack) == 0:
            return True
        else:
            return False