class Twitter:

    def __init__(self):
        self.followed = defaultdict(set)
        self.tweets = defaultdict(list)
        self.global_counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.global_counter, tweetId)) # move this to seperate block
        self.global_counter+=1 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # dumb approach grab every tweet every
        tweets = list(self.tweets[userId])
        for follow in self.followed[userId]:
            if follow != userId:
                tweets.extend(self.tweets[follow])
        return [tweet[1] for tweet in sorted(tweets, key = lambda x: -x[0])[:10]]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].discard(followeeId)
        
