#https://www.youtube.com/watch?v=CJAdCLZaISw&list=WL&index=26&t=602s

from psaw import PushshiftAPI
import config
import datetime
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("""
SELECT * FROM stock
""")

rows = cursor.fetchall()

stocks = {}

print(rows)


api = PushshiftAPI()


start_epoch=int(datetime.datetime(2021, 1, 1).timestamp())

submissions = api.search_submissions(after=start_epoch,
                            subreddit='wallstreetbets',
                            filter=['url','author', 'title', 'subreddit'])



for submission in submissions:
    #print(submission)
    #print(submission.created_utc)
    #print(submission.title)
    #print(submission.url)


    words = submission.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))


    if len(cashtags) > 0:
        print(cashtags)

        print(submission.title)