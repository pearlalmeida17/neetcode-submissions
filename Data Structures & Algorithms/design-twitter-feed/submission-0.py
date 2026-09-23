class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None: 
        
        self.count -= 1
        self.tweetMap[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        following = set(self.followMap[userId])
        following.add(userId)

        for followeeId in following:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]

                heapq.heappush(min_heap, (count, tweetId, followeeId, index - 1))

        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index >= 0:
                next_count, next_tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(min_heap, (next_count, next_tweetId, followeeId, index - 1))

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
