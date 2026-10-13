class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj ={i:[] for i in range(numCourses)}
        q = deque()

        for crs,pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs]+=1
        
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        output = []

        while q:
            temp = q.popleft()
            output.append(temp)

            for neighbor in adj[temp]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)

        if len(output)==numCourses:
            return output
        return []
        