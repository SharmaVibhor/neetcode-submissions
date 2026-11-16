class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber>26:
            c = int(columnNumber%26)
            res += chr(ord('A')+c-1)
            columnNumber -= c
            columnNumber /= 26
        
        res += chr(ord('A')+ int(columnNumber)-1)
        return res[::-1]
        