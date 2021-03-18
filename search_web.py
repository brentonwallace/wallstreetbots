from psaw import PushshiftAPI
import datetime


api = PushshiftAPI()


start_epoch=int(datetime.datetime(2021, 1, 30).timestamp())

submissions = list(api.search_submissions(after=start_epoch,
                            subreddit='wallstreetbets',
                            filter=['url','author', 'title', 'subreddit'],
                            limit=10))



for submission in submissions:
    print(submission)