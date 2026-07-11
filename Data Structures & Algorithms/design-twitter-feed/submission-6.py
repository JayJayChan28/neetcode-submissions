class Twitter:

    def __init__(self):
         self.time = 0
         self.tweet_map = defaultdict(list)
         self.user_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweet_map:
            self.tweet_map[userId].append((self.time, tweetId))
        else:
            self.tweet_map[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        res = []
        self.user_map[userId].add(userId)
        if userId in self.user_map:
            friend_ids_list = self.user_map[userId]

            for friend_id in friend_ids_list:
                #last index value of the tweet map
                if self.tweet_map[friend_id]:
                    index = len(self.tweet_map[friend_id]) - 1
                    most_rec_time, most_rec_tweetId  = self.tweet_map[friend_id][index]
                    heapq.heappush(max_heap, [-most_rec_time, most_rec_tweetId, friend_id, index - 1])
            
            while max_heap and len(res) < 10:
                most_rec_time, tweetId, friendId, index = heapq.heappop(max_heap)
                res.append(tweetId)
                if friendId in self.tweet_map:
                    if index >= 0:
                        most_rec_time, most_rec_tweetId = self.tweet_map[friendId][index]
                        heapq.heappush(max_heap, [-most_rec_time, most_rec_tweetId, friendId, index - 1])
            
            return res




    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_map:
            self.user_map[followerId].add(followeeId)
        else:
            self.user_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId and followeeId in self.user_map[followerId]:
            self.user_map[followerId].remove(followeeId)
