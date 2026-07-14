class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # legend = {')':'(', ']':'[', '}': '{'}

        for b in s:
            if b == '{' or b =='[' or b == '(' :
                    stack.append(b)
            else: 
                if stack: 
                    if ((b == '}' and stack[-1] == '{') or (b == ']' and stack[-1] == '[') or (b == ')' and stack[-1] == '(')): 
                        stack.pop()
                    else: return False
                else: return False
            
        return True if not stack else False