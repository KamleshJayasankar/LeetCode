from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        followees = set(self.following[userId]) | {userId}

        for followee_id in followees:
            if followee_id in self.tweets and self.tweets[followee_id]:
                last_idx = len(self.tweets[followee_id]) - 1
                time, tweet_id = self.tweets[followee_id][last_idx]
                min_heap.append([time, tweet_id, followee_id, last_idx - 1])

        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            time, tweet_id, followee_id, next_idx = heapq.heappop(min_heap)
            res.append(tweet_id)

            if next_idx >= 0:
                older_time, older_tweet_id = self.tweets[followee_id][next_idx]
                heapq.heappush(min_heap, [older_time, older_tweet_id, followee_id, next_idx - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)