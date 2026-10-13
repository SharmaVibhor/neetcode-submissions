class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,temp = [],[]

        if not s:
            return res
        
        def isPalindrome(s):
            return s==s[::-1]
        
        def backtrack(index):
            if index >= len(s):
                res.append(temp.copy())
            
            for i in range(index,len(s)):
                if(isPalindrome(s[index:i+1])):
                    temp.append(s[index:i+1])
                    backtrack(i+1)
                    temp.pop()
        
        backtrack(0)
        return res
        