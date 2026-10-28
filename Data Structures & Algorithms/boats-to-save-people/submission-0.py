class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        trips = 0
        people.sort()
        start, end = 0, len(people)-1

        while start<=end:
            if people[start] + people[end]<=limit:
                trips+=1
                start+=1
                end-=1
            else:
                trips+=1
                end-=1
        
        return trips
        