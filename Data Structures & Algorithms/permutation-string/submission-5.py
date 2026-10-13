class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        charSets1 = {}

        for i in range(len(s1)):
            charSets1[s1[i]] = 1 + charSets1.get(s1[i],0)

        for i in range(len(s2) - len(s1) + 1):
            charSets2 ={}
            count = 0

            for j in range(i,i+len(s1)):
                charSets2[s2[j]] = 1 + charSets2.get(s2[j],0)

                if charSets1.get(s2[j], 0) < charSets2[s2[j]] :
                    break

                if charSets1.get(s2[j], 0) == charSets2[s2[j]] :
                    count += 1
                
                
                if count == len(charSets1):
                    return True
        
        return False
        