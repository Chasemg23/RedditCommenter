import praw
import config
import time

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "RedditCommenter v1.0 by TheFunnyManJan")
	print "logged in!!!!"
	return r

def run_bot():
	for submission in subreddit.new(limit=100):
		#print "This is the original: " + submission.title + " posted by " + submission.author
		search_for_post(submission)

def check_score(post):
	if(post.score >= 1000):
		return True
	else:
		return False

def get_top_comment(post):
	targetedPost = r.get_submission(submission_id=post.id)
	print targetedPost.comments[0]

def search_for_post(submission):
	for post in subreddit.search(submission.title):
		if post.title == submission.title:
			if post.author != submission.author:
				print "Found one"
				if(check_score(post) == True):
					top_comment = get_top_comment(post)
				else:
					break

				print submission.title + submission.author.name
				print post.title + post.author.name



			else:
				print "Same person"
				break


r = bot_login()
subreddit = r.subreddit('funny')
while True:
	run_bot()
	time.sleep(5)