import requests
import requests.auth
# client_auth = requests.auth.HTTPBasicAuth('5iJNYlXAkMCoJA', '7t2AFEe42HFhfUIpg491atJrIDY')
# post_data = {"grant_type": "password", "username": "sidc9", "password": "football9"}
# headers = {"User-Agent": "python:upvote.frontpage.0.1 by sidc9"}
# response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

# data = response.json()
# token = data['access_token']

# f = open("token.txt","w")
# f.write(str(token))
# f.close()

token = "32561059-VnKy99JqihIIUWdQ5P9bgZBZXLs"


auth = "bearer " + token

# Get frontpage
get_headers = {"Authorization": auth, "User-Agent": "python:upvote.frontpage.0.1 by sidc9"}
response = requests.get("https://oauth.reddit.com", headers=get_headers)

data = response.json()

post = data['data']['children'][1]['data']['title']
sub = data['data']['children'][1]['data']['subreddit']
# item_id = data['data']['children'][1]['data']['id']
# kind = data['data']['children'][1]['kind']

fullname = data['data']['children'][1]['data']['name']

print "Upvoting: " + post + " from r/" + sub

vote_headers = {"Authorization": auth, "User-Agent": "python:upvote.frontpage.0.1 by sidc9"}
vote_data = {"id": fullname, "dir": 1}
upvote_response = requests.post("https://oauth.reddit.com/api/vote", data=vote_data, headers=vote_headers)


if upvote_response.status_code == 200:
	print "Upvoted"
else:
	print "Upvoting failed"
