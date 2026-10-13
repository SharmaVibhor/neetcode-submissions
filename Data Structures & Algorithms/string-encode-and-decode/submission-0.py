class Solution:

    def encode(self, strs: List[str]) -> str:
        res =""
        for s in strs:
            length = len(s)
            res+=str(length)
            res+="#"
            res+=s
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while(i<len(s)):
            j = i
            while(s[j]!='#'):
                j+=1

            print(s[i:j])
            length = int(s[i:j])

            i = j+length+1

            res.append(s[j+1:i])

        return res

            

        

