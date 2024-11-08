class Solution:
    def isValid(self, s: str) -> bool:
        open_map = {'(', '{',  '[', }
        close_map = {')':'(','}':'{',']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in open_map:
                stack.append(s[i])
            if s[i] in close_map:
                if len(stack) == 0:
                    stack.append(s[i])
                else:
                    if stack[-1] == close_map[s[i]]:
                        stack.pop()
                    else:
                        stack.append(s[i])
        return False if stack else True

        