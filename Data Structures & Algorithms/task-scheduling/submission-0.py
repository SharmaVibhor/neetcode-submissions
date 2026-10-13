class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        count = Counter(tasks)
        maxHeap = [c for c in count.values()]
        heapq.heapify_max(maxHeap)
        queue = deque()

        while queue or maxHeap:
            time +=1

            if not maxHeap:
                time = queue[0][1]
            else:
                cnt = heapq.heappop_max(maxHeap)-1
                if cnt:
                    queue.append([cnt,time+n])
            
            if queue and queue[0][1]==time:
                heapq.heappush_max(maxHeap,queue.popleft()[0])

        return time
        