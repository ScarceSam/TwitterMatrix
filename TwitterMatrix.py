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
go = 1

while(go == 1):

	go = 0
	#if message que is empty pull mentions
	if not tweet_queue:

		#only search back to the last pulled tweet if the all tweets sucessfully processed
		if last_tweet == 0:
			last_tweet = last_pulled

		#stop pulling mentions when a mention returned has a reply from app or it was alreay pulled
		mentions = cF.getAllNewMentions(last_tweet)

		last_tweet = mentions[0]['id']

	new_perm_display = 0 #cF.permCheck(mentions)

	mentions = cF.removeFluff(mentions)

	#save last tweet id pulled.
	#last_pulled = last tweet id in mentions

	#        thread_lenght, tweet_datetime, tweet_id, user_id, user_handle, tweet_data[8][256][3]

	#pull oldest tweet out of list
	next_tweet = mentions.pop()

	#convert each charater into RGB values
	next_tweet_RGB = cF.RGBize(next_tweet)




	#reply in cronological order

	#tell matrix an image is comming through.

	#        send serial data

	#        wait for display confirmation.

	#        take photo

	#        send photo taken message.

	#        send reply to original tweet

	#        send photo and message "Processing complete ;P"

	#        quote tweet "-username'

	#if new_permdisplay

	#        send perm display to led matrix.

	#save perm_display tweet and last tweet.

	#        delay one minute

	#        blink LED every 2 seconds.



