class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dif = [gas[i]-cost[i] for i in range(len(gas))]

        total = sum(dif)

        if total<0:
            return -1

        temp = 0
        res = 0

        for i,d in enumerate(dif):
            temp+=d
            if(temp<=0):
                temp = 0
                res = (i+1)%len(gas)

        return res


        