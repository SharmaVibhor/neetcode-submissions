class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c == "]":
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                
                stack.pop()
                
                num_str = ""
                while stack and stack[-1].isdigit():
                    num_str = stack.pop() + num_str
                
                stack.append(int(num_str) * temp)
            else:
                stack.append(c)
                
        return "".join(stack)