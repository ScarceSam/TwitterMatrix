from twython import Twython
import sys
import sqlite3
from sqlite3 import Error



########## Twython Interactions ##########

##Pull in API keys from file
from auth import (
    user_name,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

##Create twitter object
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def getFollowers(queried_user):

    data = twitter.cursor(twitter.get_followers_ids, screen_name = queried_user, return_pages=True)

    output = []

    for result in data:
        output.extend(result)

    return output


def getFriends(queried_user):

    data = twitter.cursor(twitter.get_friends_ids, screen_name = queried_user, return_pages=True)

    output = []

    for result in data:
        output.extend(result)

    return output

def getUsersTwitterData(queried_user):
    output = twitter.lookup_user(screen_name = queried_user)
    return output


def followBackTweet(user):
    message = '''{}, Thank you for the Follow Back!
\U0001f44b\U0001f600

-My Follower Thanking #TwitterBot'''.format(user)
    twitter.update_status(status=message)
    return(user, " Follow Back thanks")


def followTweet(user):
    message = '''{}, Thank you for the Follow!
\U0001f44b\U0001f600

-My Follower Thanking #TwitterBot'''.format(user)
    twitter.update_status(status=message)
    return(user, " Follow thanks")


def reFollowBackTweet(user):
    message = '''Welcome back {} \U0001f601, Thanks for the re-Follow Back!
\U0001f44b\U0001f600

-My Follower Thanking #TwitterBot'''.format(user)
    twitter.update_status(status=message)
    return(user, " reFollow Back thanks")


def reFollowTweet(user):
    message = '''Welcome back {} \U0001f601, Thanks for the re-Follow!
\U0001f44b\U0001f600

-My Follower Thanking #TwitterBot'''.format(user)
    twitter.update_status(status=message)
    return(user, " reFollow thanks")


def userName(userID):
    #print("Fetching user's screen name")
    userObject = twitter.lookup_user(user_id = userID)
    return ("@%s" % userObject[0]['screen_name'])

######### Progress Bar #########

def startProgress(title):
    global progress_x
    sys.stdout.write(title + ": [" + "-"*40 + "]" + chr(8)*41)
    sys.stdout.flush()
    progress_x = 0

def progress(x):
    global progress_x
    x = int(x * 40 // 100)
    sys.stdout.write("#" * (x - progress_x))
    sys.stdout.flush()
    progress_x = x

def endProgress():
    sys.stdout.write("#" * (40 - progress_x) + "]\n")
    sys.stdout.flush()

########## Database manipulation ##########

def sql_connection(fileName):
    try:
        con = sqlite3.connect(fileName)
        return con
    except Error:
        print(Error)

def sql_followers_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE connections(user_IDs int PRIMARY KEY, screen_name text, isFollower bool, followDate text, isFriend bool, friendDate text, thanked bool, rethanked bool)")
    con.commit()

def total_rows(cursor, table_name, print_out=False):
    """ Returns the total number of rows in the database """
    cursor.execute('SELECT COUNT(*) FROM {}'.format(table_name))
    count = cursor.fetchall()
    if print_out:
        print('\nTotal rows: {}'.format(count[0][0]))
    return count[0][0]

############## colors ################

color = {' ': '000000', '!': 'FFFFFF',
	'"': '212121', '#': '616161', '$': '9E9E9E', '%': 'E0E0E0', '&': 'F5F5F5',
	'\'': '3E2723', '(': '5D4037', ')': '795548', '*': 'A1887F', '+': 'D7CCC8',
	',': '880E4F', '-': 'C2185B', '.': 'E91E63', '/': 'F06292', '0': 'F8BBD0',
	'1': 'B71C1C', '2': 'D32F2F', '3': 'F44336', '4': 'E57373', '5': 'FFCDD2',
	'6': 'BF360C', '7': 'E64A19', '8': 'FF5722', '9': 'FF8A65', ':': 'FFCCBC',
	';': 'E65100', '<': 'F57C00', '=': 'FF9800', '>': 'FFB74D', '?': 'FFE0B2',
	'@': 'FF6F00', 'A': 'FFA000', 'B': 'FFC107', 'C': 'FFD54F', 'D': 'FFECB3',
	'E': 'F57F17', 'F': 'FBC02D', 'G': 'FFEB3B', 'H': 'FFF176', 'I': 'FFF9C4',
	'J': '827717', 'K': 'AFB42B', 'L': 'CDDC39', 'M': 'DCE775', 'N': 'F0F4C3',
	'O': '33691E', 'P': '689F38', 'Q': '8BC34A', 'R': 'AED581', 'S': 'DCEDC8',
	'T': '1B5E20', 'U': '388E3C', 'V': '4CAF50', 'W': '81C784', 'X': 'C8E6C9',
	'Y': '004D40', 'Z': '00796B', '[': '009688', '\\': '4DB6AC', ']': 'B2DFDB',
	'^': '006064', '_': '0097A7', '`': '00BCD4', 'a': '4DD0E1', 'b': 'B2EBF2',
	'c': '01579B', 'd': '0288D1', 'e': '03A9F4', 'f': '4FC3F7', 'g': 'B3E5FC',
	'h': '0D47A1', 'i': '1976D2', 'j': '2196F3', 'k': '64B5F6', 'l': 'BBDEFB',
	'm': '1A237E', 'n': '303F9F', 'o': '3F51B5', 'p': '7986CB', 'q': 'C5CAE9',
	'r': '311B92', 's': '512DA8', 't': '673AB7', 'u': '9575CD', 'v': 'D1C4E9',
	'w': '4A148C', 'x': '7B1FA2', 'y': '8E24AA', 'z': 'AB47BC', '{': 'CE93D8',
	'|': '000000', '}': '000000', '~': '000000'}



########### getting mentions ############

def getAllNewMentions(lastTweetID):
	#lastTweetID = 1221548022816858112
	lastTweetFound = 0
	data = []
	oldestTweetID = 0

	while not lastTweetFound:

		if oldestTweetID:
			data += twitter.get_mentions_timeline(tweet_mode='extended', trim_user = 1, since_id = (lastTweetID - 1), max_id = (oldestTweetID - 1))
		else:
			data += twitter.get_mentions_timeline(tweet_mode='extended', trim_user = 1, since_id = (lastTweetID - 1)) #since_id = 1212247345384935424)

		for item in data:
			oldestTweetID = item['id']
			if item['id'] == lastTweetID:
				lastTweetFound += 1
				data.pop()

	#print(lastTweetFound) #dev

	number = 0 #testing

	for item in data: #testing
		if number == item['id']: #testing
			print('FAIL') #testing
		number = item['id'] #testing


	#if !lastTweetFound:

	#print(len(data)) #dev

	#for item in data: #reversed(data):
	#	print(item['id'], '\n', item['full_text'], end='\n\n')
	return data
