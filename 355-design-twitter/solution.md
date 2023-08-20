# 355. Design Twitter

## Desc

> Implement the **Twitter** class

> **Twitter()** initializes your twitter object

> **void postTweet(int userId, int tweetId)** composes a new tweet with ID by the user.

> Each call to this function will be made with a unique **tweetId**

> **getNewsFeed(int userId)** retrieves the 10 most recent tweet IDs in the user's news feed.

> Each item is the news feed must be posted by users who the user follwed or by the user themself

> Tweets must be **ordered from most recent to least recent**

> **follow(followerId, followeeId)** the user with id followerId started following the user with Id followeeId

> **unfollow(followerId, followeeId)** the user followerId started unfollowing the user followeeId

## Idea

> We can use a counter with two HashMap to solve this problem

> We post a new tweet, we simply add a **(userId, (counter, tweetId))** pair to the tweets Map

> When getnewsfeed, we will simply use a maxheap to help us the filter the 10 most recent tweets based on the counts

> we will first get all the tweets from the users that the user follows, and use the maxheap to get the result

> follow will simply add the followeeId to the followMap of that user

> same for unfollow

## Complexity

### TC: O(nlogn)

### SC: O(nm)