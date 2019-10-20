import praw
import pandas as pd
from sklearn.utils import shuffle

reddit = praw.Reddit(client_id='<14 character client id', \
                     client_secret='<27 character client secret>', \
                     user_agent='<name you gave your application>', \
                     username='<reddit username>', \
                     password='<reddit password>')

react_posts = []
reactjsposts = reddit.subreddit('reactjs').hot(limit=1000)
for post in reactjsposts:
    react_posts.append([post.title, post.selftext, post.subreddit])

react_df = pd.DataFrame(react_posts, columns=['Title', 'Body', 'SubReddit'])
print(f'Total rows in react {react_df.shape[0]}')
angular_posts = []
angularposts = reddit.subreddit('angular').hot(limit=1000)
for post in angularposts:
    angular_posts.append([post.title, post.selftext, post.subreddit])

angular_df = pd.DataFrame(angular_posts, columns=['Title', 'Body', 'SubReddit'])
print(f'Total rows in angular {angular_df.shape[0]}')

vuejs_posts = []
vueposts = reddit.subreddit('vuejs').hot(limit=1000)
for post in vueposts:
    vuejs_posts.append([post.title, post.selftext, post.subreddit])

vue_df = pd.DataFrame(vuejs_posts, columns=['Title', 'Body', 'SubReddit'])
print(f'Total rows in vue {vue_df.shape[0]}')

df = pd.concat([react_df, angular_df, vue_df])
df = shuffle(df)
df.reset_index(inplace=True, drop=True)
print(df.shape)
df.to_csv('reddit_posts.csv', index=False, header=True)