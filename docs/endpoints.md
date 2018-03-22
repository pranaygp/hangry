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

## Restaurant

## Location

## Serves

## Cuisine

## Photo

## Rating
