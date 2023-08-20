import collections
import heapq


class Twitter:
    def __init__(self):
        self.tweetsMap = collections.defaultdict(list)
        self.followMap = collections.defaultdict(set)
        self.count = 0

    def postTweet(self, userId, tweetId):
        self.tweetsMap[userId].append((self.count, tweetId))

        self.count -= 1

    def getNewsFeed(self, userId):
        self.follow(userId, userId)

        pq, res = [], []

        for user in self.followMap[userId]:
            if self.tweetsMap[user]:
                tweets = self.tweetsMap[user]
                idx = len(tweets) - 1

                count, tweet = tweets[idx]

                heapq.heappush(pq, (count, tweet, tweets, idx))

        while pq and len(res) < 10:
            count, tweet, tweets, idx = heapq.heappop(pq)

            res.append(tweet)

            if idx == 0:
                continue

            idx -= 1

            count, tweet = tweets[idx]

            heapq.heappush(pq, (count, tweet, tweets, idx))

        return res

    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
