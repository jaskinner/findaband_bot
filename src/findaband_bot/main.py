import praw
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

# setup spotipy
scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# setup praw/reddit
# reddit = praw.Reddit('bot1')
# subreddit = reddit.subreddit("test")

# load data
map = open("data/map.json")
data = json.load(map)
map.close

artist = ""

def capture_comment():
    return

def parse_artist_from_comment(comment):
    return

def get_artist_from_map(artist, map):
    return

def get_related_artist(retrieved_artist):
    return 

def get_artist_data(artist):
    return

def form_new_reply(artist_data):
    return

def write_reply(reply_data):
    return

    # searchQuery = ""
    # track_id = sp.search(q="artist:" + requestedArtist + " track:" +
    #                      searchQuery, type='track', limit=1)
    # if track_id:
    #     return track_id["tracks"]


# for comment in subreddit.stream.comments(skip_existing=True):
#     if "plzfind" in comment.body:
#     	comment.reply(body=findsomething())

# crawl comments
# get artist from comment
# find artist in map
# find related artist 
# get artist properties and links
# form new reply with artist info
# write reply to new comment