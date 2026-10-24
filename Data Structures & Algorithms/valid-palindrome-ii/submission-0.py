class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s1: str,start,end, canSkip: bool):
            while start<end:
                if s1[start] == s1[end]:
                    start+=1
                    end-=1
                elif canSkip:
                    res = isPalindrome(s1,start,end-1, False) or isPalindrome(s1,start+1,end,False)
                    return res
                else:
                    return False
            
            return True
        
        return isPalindrome(s,0,len(s)-1,True)