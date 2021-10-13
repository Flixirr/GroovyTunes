# Example request

For route /api/v1/users/auth/register/ PUSH
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

For route /api/v1/users/auth/api-token-auth/ PUSH
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

For route /api/v1/users/auth/user/ GET
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

For route /api/v1/users/auth/logout/ POST
```json
header:
KEY		VALUE
Authorization	Token 6474f20911b0342eb2e5a6afb65f756cf43c9f37
reply:
{
    "detail": "Successfully logged out."
}
```

For route /api/v1/users/auth/login/ POST
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

User Examples

Post user:

URL = "http://127.0.0.1:8000/api/user"
data = {'firstName': 'Max',
		'lastName':'Musterman',
		'userName':'testUser',
        'email':'test@test.com',
        'password': 'test'}
r = requests.put(url = URL, json = data)

The other things work like in playlist

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
