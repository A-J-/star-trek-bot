import praw,username

userAgent = ("StarTrekBot 0.1")
r = praw.Reddit(user_agent = userAgent)
r.login(username.main())
subreddit = r.get_subreddit("ftlgame")

for thread in subreddit.get_new(limit = 5):

	print "Title: ",thread.title
	print "Score: ",thread.score
	print
	print
	
