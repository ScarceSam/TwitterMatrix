import customFunctions as cF

last_pulled = 1221548022816858112
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
		if last_pulled != 0:
			last_tweet = last_pulled

		#stop pulling mentions when a mention returned has a reply from app or it was alreay pulled
		mentions = cF.getAllNewMentions(last_tweet)

	new_perm_display = 0 #cF.permCheck(mentions)

	#mentions = removeFluff(mentions)

	new_perm_display = 0 #cF.permCheck(mentions)

	mentions = cF.removeFluff(mentions)

		#save last tweet id pulled.
		#last_pulled = last tweet id in mentions



	#clean up data, tweet save into an object save only tweets that have @LED_matrix at beginning of thread
	

	#        save tweet id if it's is from @scarcesam and says "@LED_Matrix... perm display this one!"

	#        thread_lenght, tweet_datetime, tweet_id, user_id, user_handle, tweet_data[8][256][3]

	#        convert each charater into RGB values



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



