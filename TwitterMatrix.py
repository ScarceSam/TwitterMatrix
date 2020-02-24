import customFunctions as cF

last_pulled = 1221548022816858112
last_tweet = 0
new_perm_display = 0
tweet_queue = 0

#check for save file
#if save file:

	#pull saved info
#	last_pulled = file.last_pulled
#	if perm_display = file.permdisplay:
#		new_perm_display = 1

while(go == 1):

	#if message que is empty pull mentions
	if not tweet_queue:

		#only search back to the last pulled tweet if the all tweets sucessfully processed
		if last_tweet == 0:
			last_tweet = last_pulled

		#stop pulling mentions when a mention returned has a reply from app or it was alreay pulled
		mentions = cF.getAllNewMentions(last_tweet)

		if len(mentions):

			#save last ID pulled
			last_pulled = mentions[0]['id']

			tweet_queue = len(mentions)

			new_perm_display = 0 #cF.permCheck(mentions)

			#remove all tweets from list that are not direct mentions
			mentions = cF.removeFluff(mentions)

			tweet_queue = len(mentions)

	if tweet_queue:

		#pull oldest tweet out of list
		next_tweet = mentions.pop()

		tweet_queue = len(mentions)

		#convert each charater into RGB values
		next_tweet_RGB = cF.RGBize(next_tweet)

		#is matrix attached? which serial port? available?

		#send serial data

		#wait for display confirmation. take photo

		#send photo taken message.

		#send reply to original tweet

		#send photo and message "Processing complete ;P"

		#quote tweet "-username'

		last_tweet = next_tweet['id']

		#if new_permdisplay

			#send perm display to led matrix.

			#save perm_display tweet and last tweet.

		#delay one minute

		#blink LED every 2 seconds.


		#Print(tweet info)
		print(len(mentions))
		print(next_tweet)
		#print(next_tweet_RGB)
		for i in range(16):
			for j in range(16):
				if j == 15:
					print(next_tweet_RGB[j + (16 * i)])
				else:
					print(next_tweet_RGB[j + (16 * i)], end = ' , ')


