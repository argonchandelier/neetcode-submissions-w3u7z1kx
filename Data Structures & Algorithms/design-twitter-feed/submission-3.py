import heapq as hq

class Twitter:

    def __init__(self):
        self.tweets = [[] for _ in range(100)]
        self.followers = [set() for _ in range(100)]
        self.orderCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        hq.heappush(self.tweets[userId-1], [-self.orderCount, tweetId])
        self.orderCount += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followers[userId-1]
        relTweets = self.tweets[userId-1][:]
        for follower in followers:
            #print(f"{userId = } follows {follower}")
            relTweets += self.tweets[follower-1]
        hq.heapify(relTweets)

        #for i in range(min(10, len(relTweets))): # Tweets of user <- change
        #    toShow.append(-relTweets[i])
        recentTweets = hq.nsmallest(min(10, len(relTweets)), relTweets)
        
        #print(f"tweets: {self.tweets}")
        return [recTw[1] for recTw in recentTweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers[followerId-1].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId-1].discard(followeeId)
