import requests
import json

#Get your toke here after logging in: https://developer.webex.com/docs/api/getting-started
token = 'MGYxODlkNjctNzI2OS00ZmQ0LThlYTYtYWQ4ZjFjZGIyMjFiYWM5ZjlhMjktZDlh_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'

##Create a Team##
url = 'https://api.ciscospark.com/v1/teams'
headers = {'Authorization':f'Bearer {token}',
            'Content-Type':'application/json'}

body = {
    "name" : "Test Team"
}

#post_response = requests.post(url, headers=headers, data=json.dumps(body)).json()
#print(post_response)

get_response = requests.get(url, headers=headers).json()
#teamId = get_response['items'][0]['id']
teams = get_response['items']
for team in teams:
    if team['name'] == 'Test Team':
        teamId = team['id']

####### Create a room #####
room_url = 'https://api.ciscospark.com/v1/rooms'
room_body = {
    "title" : "Test Room",
    "teamId" : teamId
}

#room_post = requests.post(room_url, headers=headers, data=json.dumps(room_body)).json()

get_rooms = requests.get(room_url, headers=headers).json()
rooms = get_rooms['items']
for room in rooms:
    if room['title'] == 'Test Room':
        roomId = room['id']

# #### POST A MESSAGE TO THE ROOM #####
msg_url = 'https://api.ciscospark.com/v1/messages'
message_body = {
    "text": "Hi there, this is a test",
    "roomId" : roomId
}

message_post = requests.post(msg_url, headers=headers, data=json.dumps(message_body)).json()