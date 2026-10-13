class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if (len(hand)%groupSize!=0):
            return False

        count = Counter(hand)

        for key in sorted(count):
            if count[key]>0:
                freq = count[key]

                for i in range(key,key+groupSize):
                    if count[i]<freq:
                        return False
                    count[i]-=freq
        
        return True



        