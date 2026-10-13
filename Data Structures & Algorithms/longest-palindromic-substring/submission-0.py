class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s

        res = 0
        resStr = ""

        for i in range(len(s)):
            #odd
            l,r = i,i

            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1>len(resStr)):
                    res = r-l+1
                    resStr = s[l:r+1]
                l-=1
                r+=1

            #even
            l,r = i,i+1

            while(l>=0 and r<len(s) and s[l]==s[r]):
                if(r-l+1>res):
                    res = r-l+1
                    resStr = s[l:r+1]
                l-=1
                r+=1


        return resStr
        