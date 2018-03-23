# Endpoint Documentation


## User

**Endpoint**

    GET /users

This returns all of the users in our Users table. It returns each column for each user.

**Response**
```
{
    "users": [
        {
            "email": "abdalla6@illinois.edu",
            "latitude": 40.1059,
            "longitude": -88.243385,
            "name": "Abdi Abdalla",
            "password": "password",
            "user_id": 1,
            "username": "abdi"
        },
        .
        .
        .
    ]
}
```
**Endpoint**

    GET /user/id/<user_id>

This searches the Users relation by the user_id criterion, and either returns the corresponding user or nothing.

**Response**
```
{
    "status": "success",
    "user": {
        "email": "abdalla6@illinois.edu",
        "latitude": 40.1059,
        "longitude": -88.243385,
        "name": "Abdi Abdalla",
        "password": "password",
        "user_id": 1,
        "username": "abdi"
    }
}
```

**Endpoint**

    DELETE /user/username/<user_id>

This searches the Users relation by the user_id criterion, and either deletes the corresponding user or does nothing.

**Response**

```
{
    "message": "Successfully deleted user!",
    "status": "success"
}
```


**Endpoint**

    GET /user/username/<username>

This searches the Users relation by the username criterion, and either returns the corresponding user or nothing.
**Response**
```
{
    "status": "success",
    "user": {
        "email": "abdalla6@illinois.edu",
        "latitude": 40.1059,
        "longitude": -88.243385,
        "name": "Abdi Abdalla",
        "password": "password",
        "user_id": 1,
        "username": "abdi"
    }
}
```

**Endpoint**

    DELETE /user/username/<username>

This searches the Users relation by the username criterion, and either deletes the corresponding user or does nothing.

**Response**

```
{
    "message": "Successfully deleted user!",
    "status": "success"
}
```

**Endpoint**

    POST /user

Creates a new user in the User table given the correct input.

**Input**

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| email | string |   **Required** | test1@gmail.com
| username | string |   **Required** | test1
| password | string | **Required** | fakepassword
| name | string | Can be NULL | Test Person
| latitude | float | Can be NULL | 40.12891
| longitude | float | Can be NULL | -87.3202

This input must be passed in the form of JSON, as below:

```
{
	"username" : "test1",
	"email" : "test1@gmail.com",
	"password" : "fakepassword",
	"name" : "Test Person",
	"latitude" : 40.00,
	"longitude" : -87.00
}
```

**Response**

```
{
    "message": "Created new user!",
    "status": "success"
}
```

## Auth

**Endpoint**

    POST /login

Logs a user in, given correct credentials, and creates a session for the user. Requires the username and password as input.

**Input**

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| username | string |   **Required** | test1
| password | string | **Required** | fakepassword

```
{
    "username": "test1",
    "password": "fakepassword"
}
```

**Response**

```
{
    "message": "User [username] successfully logged in!",
    "status": "success"
}
```

**Endpoint**

    GET /logout

Logs a user out, and ends their session.

**Response**

```
{
    "message": "User [username] successfully logged out!",
    "status": "success"
}
```

**Endpoint**

    POST /signup

Intended for the signup flow. Creates a new user in the User table given the correct input (and the username and email aren't already taken).

**Input**

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| email | string |   **Required** | test1@gmail.com
| username | string |   **Required** | test1
| password | string | **Required** | fakepassword

This input must be passed in the form of JSON, as below:

```
{
	"username" : "test1",
	"email" : "test1@gmail.com",
	"password" : "fakepassword"
}
```

**Response**

```
{
    "message": "Created new user!",
    "status": "success"
}
```

## Restaurant

## Location

## Serves

## Cuisine

## Photo

**Endpoint**

    GET /photos/user/<user_id>

This searches the Photos relation by the user_id criterion, and returns the list of photos by the user.

**Response**

```
{
    "photos": [
        {
            "photo_path": "https://i.imgur.com/VekfqoA.jpg",
            "restaurant_id": 4,
            "user_id": 4
        },
        .
        .
        .
    ],
    "status": "success"
}
```

**Endpoint**

    GET /photos/restaurant/<restaurant_id>

This searches the Photos relation by the restaurant_id criterion, and returns the list of photos associated with the restaurant.

**Response**

```
{
    "photos": [
        {
            "photo_path": "https://i.imgur.com/VekfqoA.jpg",
            "restaurant_id": 4,
            "user_id": 4
        },
        .
        .
        .
    ],
    "status": "success"
}
```

**Endpoint**

    DELETE /photos/<photo_id>

This searches the Photos relation by the photo_id criterion, and deletes the corresponding photo from our database.

**Response**

```
{
    'status' : 'success',
    'message' : 'Successfully deleted photo!'
}
```

**Endpoint**

    POST /photos

Upload a photo to our database, and link it with a user and restaurant.

**Input**

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| user_id | string |   **Required** | 4
| restaurant_id | string |   **Required** | 76
| image_url | string | **Required** | "https://i.imgur.com/dlkfslA.jpg"

This input must be passed in the form of JSON, as below:

```
{
	"user_id" : 4,
	"restaurant_id" : 76,
	"image_url" : "https://i.imgur.com/dlkfslA.jpg"
}
```

**Response**

```
{
    "message": "Successfully uploaded image!",
    "status": "success"
}
```

## Rating
