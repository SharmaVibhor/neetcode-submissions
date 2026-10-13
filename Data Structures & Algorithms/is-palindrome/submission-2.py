class Solution:
    def isvalidchar(self,c):
        return (ord('a')<=ord(c)<=ord('z')) or (ord('A')<=ord(c)<=ord('Z')) or (ord('0')<=ord(c)<=ord('9'))
    
    
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end =len(s)-1

        while start<end:
            while not self.isvalidchar(s[start]) and start<end:
                start+=1
            while not self.isvalidchar(s[end]) and end>start:
                end-=1
    
            if s[start].lower() != s[end].lower():
                return False
            start+=1
            end-=1
        return True