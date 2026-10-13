class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) # i:[]  
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        res = []
        for time,tweet in self.tweets[userId]:
            heapq.heappush_max(minheap,(time,tweet))
        
        for follower in self.followers[userId]:
            for time,tweet in self.tweets[follower]:
                heapq.heappush_max(minheap,(time,tweet))
        
        while minheap and len(res)<10:
            res.append(heapq.heappop_max(minheap)[1])
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
