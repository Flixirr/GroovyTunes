# Example request

For route /api/users/auth/register/ PUSH
```json
{
    "email": "johnnytest@aa.aa",
    "password1": "Testownik112",
    "password2": "Testownik112"
}
reply:
{
    "key": "69bd0b781517098c3a782737f64554381dd9411b"
}
```

For route /api/users/auth/api-token-auth/ PUSH
```json
body:
KEY		VALUE
username:	johannes
password	password321
reply:
{
   "token": "6474f20911b0342eb2e5a6afb65f756cf43c9f37"
}
```

For route /api/users/auth/user/ GET
```json
header:
KEY		VALUE
Authorization	Token 6474f20911b0342eb2e5a6afb65f756cf43c9f37
reply:
{
    "pk": 6,
    "username": "johannes",
    "email": "johannes.schleicher1998@gmail.com",
    "first_name": "",
    "last_name": ""
}
```

For route /api/users/auth/logout/ POST
```json
header:
KEY		VALUE
Authorization	Token 6474f20911b0342eb2e5a6afb65f756cf43c9f37
reply:
{
    "detail": "Successfully logged out."
}
```

For route /api/users/auth/login/ POST
```json
body:
KEY		VALUE
email		johannes.schleicher1998@gmail.com
password	password321
reply:
{
    "key": "6474f20911b0342eb2e5a6afb65f756cf43c9f37"
}
```
Playlist example requests

Get all Playlists:
	URL = "http://127.0.0.1:8000/api/playlist"
	r = requests.get(url = URL)
	data = r.json()

	Return (Example for 2 playlists):
		[{"id": 1, "name": "coolPlaylist", "rating_sum": 5, "rating_number": 1, "user": 1}, {"id": 2, "name": "coolPlaylist2", "rating_sum": 4, "rating_number": 2, "user": 1}]


Get playlist with id = 1:
	URL = "http://127.0.0.1:8000/api/playlist/1"
	r = requests.get(url = URL)
	data = r.json()

	Return:
		{'id': 13, 'name': 'cool2', 'rating_sum': 5, 'rating_number': 1, 'user': 1}


Post new Playlist:
	URL = "http://127.0.0.1:8000/api/playlist"
	data = {'user': 1,
			'name':'coolPlaylistName',
			'rating_sum':6,
			'rating_number':2}
	r = requests.post(url = URL, json = data)


Delete all Playlists:
	URL = "http://127.0.0.1:8000/api/playlist"
	r = requests.delete(URL)

Delete playlist with id = 1:
	URL = "http://127.0.0.1:8000/api/playlist/1"
	r = requests.delete(url = URL)
	

Put playlist at id = 1:
URL = "http://127.0.0.1:8000/api/playlist/1"
data = {'user': 1,
        'name':'coolPlaylistName',
		'rating_sum':6,
		'rating_number':2}
r = requests.put(url = URL, json = data)


Post user:

URL = "http://127.0.0.1:8000/api/user"
data = {'firstName': 'Max',
		'lastName':'Musterman',
		'userName':'testUser',
        'email':'test@test.com',
        'password': 'test'}
r = requests.put(url = URL, json = data)


Get all playlists for user with id = 1:
api/user/playlists/1


Get playlist rating for user.id = 1 and playlist.id = 2:
api/playlist_rating/2/1


Rate a playlist:
URL = "http://127.0.0.1:8000/api/rate_playlist"
data = {"user": 1, "playlist": 4, "rating": 5}

r = requests.post(url = URL, json=data)
(you can always use a Post request, if the rating is already created it will be changed and if it is not created it will be created)

Get/Delete all comments for playlist with id = 1:
api/playlist/comments/1

Get/Delete/Post one comment with id = 1:
api/comment/1

Get/Delete all comments:
api/comment

Put new comment:
URL = "http://127.0.0.1:8000/api/comment"
data = {"user": 1, "playlist": 4, "comment_text": 'a cool text'}

r = requests.put(url = URL, json=data)


# New User model:

For route /api/users/rest/register POST
```json
body:
KEY		VALUE
email		max.mustermann@yahoo.de
username	hirsch11
first_name	max
last_name	mustermann
password	password321
password2	password321
reply:
{
    "response": "successfully registered new user.",
    "email": "max.mustermann@yahoo.de",
    "username": "hirsch11",
    "first_name": "max",
    "last_name": "mustermann",
    "pk": 10,
    "token": "9a0f3ecbd826ea2eca3fb72ddec91d3f52f97009"
}
```

For route /api/users/rest/login POST
```json
body:
KEY		VALUE
email		max.mustermann@yahoo.de
username	hirsch11
first_name	max
last_name	mustermann
password	password321
password2	password321
reply:
{
    "response": "Successfully authenticated.",
    "pk": 10,
    "email": "max.mustermann@yahoo.de",
    "token": "9a0f3ecbd826ea2eca3fb72ddec91d3f52f97009"
}
```

For route /api/users/rest/check_if_account_exists GET
```json
Params:
KEY		VALUE
email		max.mustermann@yahoo.de
reply:
{
    "response": "max.mustermann@yahoo.de"
}
# If account does not exist: "response": "Account does not exist"
# alternative params into address: http://127.0.0.1:8000/api/users/rest/check_if_account_exists/?email=max.@yahoo.de
```

For route /api/users/rest/properties GET
```json
Headers:
KEY		VALUE
Authorization	Token 9a0f3ecbd826ea2eca3fb72ddec91d3f52f97009
reply:
{
    "pk": 10,
    "email": "max.mustermann@yahoo.de",
    "username": "hirsch11",
    "first_name": "max",
    "last_name": "mustermann"
}
```

For route /api/users/rest/properties/update PUT
```json
Headers:
KEY		VALUE
Authorization	Token 9a0f3ecbd826ea2eca3fb72ddec91d3f52f97009
Body:
KEY		VALUE
username	sheep12
first_name	dieter
last_name	missing
email		max.mustermann@yahoo.de
reply:
{
    "response": "Account update success"
}
```

For route /api/users/rest/change_password PATCH
```json
Headers:
KEY		VALUE
Authorization	Token 9a0f3ecbd826ea2eca3fb72ddec91d3f52f97009
Body:
KEY			VALUE
old_password		password321
new_password		password123
confirm_new_password	password123
reply:
{"response":"successfully changed password"}
```

http://127.0.0.1:8000/api/users/rest/logout POST
```json
Headers:
KEY		VALUE
Authorization	Token 9a0f3ecbd826ea2eca3fb72ddec91d3f52f97009
reply:
{"sheep12 got logged out"}
```

# How to run?

For backend server
```
cd backend/
pipenv install
pipenv shell
python manage.py runserver
```

For frontend server

```
cd frontend/
npm install
npm start
```

In order for the application to work you have to have both servers running.
