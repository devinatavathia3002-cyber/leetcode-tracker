# Last updated: 4/4/2026, 12:17:17 AM
1class Twitter:
2
3    def __init__(self):
4        self.followers = defaultdict(set) # map user --> [followers]
5        self.users = defaultdict(list) # map user --> ([time, tweet])
6        self.time = 0 # time
7        
8    def postTweet(self, userId: int, tweetId: int) -> None:
9        self.users[userId].append([self.time, tweetId])
10        self.time -= 1
11
12    def getNewsFeed(self, userId: int) -> List[int]:
13        self.followers[userId].add(userId)
14
15        res = []
16        minHeap = []
17
18        for follower in self.followers[userId]:
19            if self.users[follower]:
20                index = len(self.users[follower]) - 1
21                time, tweet = self.users[follower][index]
22                heapq.heappush(minHeap, [time, tweet, follower, index - 1])
23        
24        while minHeap and len(res) < 10:
25            time, tweet, follower, index = heapq.heappop(minHeap)
26            res.append(tweet)
27            if index >= 0:
28                time, tweet = self.users[follower][index]
29                heapq.heappush(minHeap, [time, tweet, follower, index - 1])
30        
31        return res
32
33    def follow(self, followerId: int, followeeId: int) -> None:
34        self.followers[followerId].add(followeeId)
35
36    def unfollow(self, followerId: int, followeeId: int) -> None:
37        if followeeId in self.followers[followerId]:
38            self.followers[followerId].remove(followeeId)
39