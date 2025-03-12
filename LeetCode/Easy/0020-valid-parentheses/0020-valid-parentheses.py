class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0: return False
                j = stack.pop()
                if j + i == "()" or j + i == "[]" or j + i == "{}":
                    pass
                else: return False
        if len(stack) != 0: return False
        return True

        