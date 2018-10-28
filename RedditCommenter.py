import praw
import config
import time

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Testing new bot")
	print "logged in!!!!"
	return r

def run_bot(r):
	for submission in subreddit.new(limit=100):
		#print "This is the original: " + submission.title + " posted by " + submission.author
		search_for_post(submission)

def search_for_post(submission):
	for post in subreddit.search(submission.title, limit=100):
		if post.title == submission.title:
			if post.author != submission.author:
				print "Found one"
				time.sleep(5)
				print submission.title + submission.author.name
				print post.title + post.author.name
			else:
				print "Same person"


r = bot_login()
subreddit = r.subreddit('funny')
while True:
	run_bot(r)
	time.sleep(5)