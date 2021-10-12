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
