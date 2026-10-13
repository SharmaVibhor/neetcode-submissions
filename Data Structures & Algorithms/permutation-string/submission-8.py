class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        if len(s2)<len(s1):
            return False
        map1 = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
        map2 = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}

        for c in s1:
            map1[c]+=1
        
        for i in range(length):
            map2[s2[i]]+=1

        print(map1)
        print(map2)
        if map1==map2:
            return True

        for i in range(1,len(s2)-len(s1)+1):
            map2[s2[i-1]]-=1
            map2[s2[i+length-1]]+=1

            #print(map2)
            if map1==map2:
                return True

        return False