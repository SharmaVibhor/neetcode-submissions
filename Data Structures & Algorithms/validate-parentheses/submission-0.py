class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            
            else :

                if not stack:
                    return False

                top = stack.pop()
                if (top == '(' and s[i]!=')') or (top == '{' and s[i]!='}') or (top == '[' and s[i]!=']'):
                    return False
            
        return len(stack) == 0
            
        