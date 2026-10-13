class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums_list=nums
        self.k = k

        if self.nums_list:
            heapq.heapify(self.nums_list)
        
        while len(self.nums_list)>self.k:
            heapq.heappop(self.nums_list)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums_list,val)

        if(len(self.nums_list)>self.k):
            heapq.heappop(self.nums_list)

        return self.nums_list[0]
        
