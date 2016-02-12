import requests
import requests.auth
import json
import sys

try:
	with open('reddit_bot.json') as data_file:
		config = json.load(data_file)
except:
	print "Couldn't load credentials file"
	exit(1)


APP_KEY = config['APP_KEY']
APP_SECRET =config['APP_SECRET']
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']

print "\nAuthenticating...\n"

client_auth = requests.auth.HTTPBasicAuth(str(APP_KEY), str(APP_SECRET))
post_data = {"grant_type": "password", "username": str(USERNAME), "password": str(PASSWORD)}
headers = {"User-Agent": "python:upvote.frontpage.0.1 by sidc9"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

data = response.json()
token = data['access_token']

# f = open("token.txt","w")
# f.write(str(token))
# f.close()

#token = "32561059-VnKy99JqihIIUWdQ5P9bgZBZXLs"

print "Success!\n\nHiding 25 posts from Front Page..."
exit(1)
auth = "bearer " + token

# Get frontpage
get_headers = {"Authorization": auth, "User-Agent": "python:upvote.frontpage.0.1 by sidc9"}
response = requests.get("https://oauth.reddit.com", headers=get_headers)

data = response.json()
failed_list = list()
name_list = ""

for i in range(0,25):
	post = data['data']['children'][i]['data']['title']
	sub = data['data']['children'][i]['data']['subreddit']
	# item_id = data['data']['children'][1]['data']['id']
	# kind = data['data']['children'][1]['kind']

	fullname = data['data']['children'][i]['data']['name']

	try:
		print "#",i, "  " + post + "\n\tfrom r/" + sub + "\n"

	except:
		# To catch unrecognized character encodings
		print "#",i, "  !! couldn't print macha !! \n"

	vote_headers = {"Authorization": auth, "User-Agent": "python:upvote.frontpage.0.1 by sidc9"}	
	name_list = name_list + fullname

	if( i != 24):
		name_list = name_list + ","


hide_data = {"id": name_list}
hide_response = requests.post("https://oauth.reddit.com/api/hide", data=hide_data, headers=vote_headers)

if hide_response.status_code != 200:
	failed_list.append(i)


if failed_list:
	print "Failed :( : " + failed_list
else:
	print "Done! :) "
