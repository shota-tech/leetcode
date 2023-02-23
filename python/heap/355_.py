# https://leetcode.com/problems/design-twitter/

from collections import defaultdict
import heapq


class Twitter:
    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        min_heap = []

        self.follows[userId].add(userId)
        for foloweeId in self.follows[userId]:
            if foloweeId not in self.tweets:
                continue

            index = len(self.tweets[foloweeId]) - 1
            cnt, tweetId = self.tweets[foloweeId][index]
            heapq.heappush(min_heap, (cnt, tweetId, foloweeId, index - 1))

        while min_heap and len(feed) < 10:
            _, tweetId, foloweeId, index = heapq.heappop(min_heap)
            feed.append(tweetId)

            if index >= 0:
                cnt, tweetId = self.tweets[foloweeId][index]
                heapq.heappush(min_heap, (cnt, tweetId, foloweeId, index - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
