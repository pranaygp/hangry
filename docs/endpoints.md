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

**Endpoint**

    GET /restaurants

This returns all of the restaurants in our Restaurants table. It returns each column for each restaurant.

**Response**
```
{
    "restaurants": [
        {
            "restaurant_id": 1,
            "restaurant_name": "McDonalds"
        },
        .
        .
        .
    ]
}
```
**Endpoint**

    GET /restaurant/id/<restaurant_id>

This searches the Restaurant relation by the restaurant_id criterion, and either returns the corresponding restaurant or nothing.

**Response**
```
{
    "status": "success",
    "restaurant": {
        "restaurant_id": 1,
        "restaurant_name": "McDonalds"
    }
}
```

**Endpoint**

    GET /restaurant/name/<restaurant_name>

This searches the Restaurant relation by the restaurant_name criterion, and either returns all corresponding restaurants or nothing.

**Response**
```
{
    "restaurants": [
        {
            "restaurant_id": 1,
            "restaurant_name": "McDonalds"
        },
        .
        .
        .
    ]
}
```

**Endpoint**

    DELETE /restaurant/id/<restaurant_id>

This searches the Restaurant relation by the restaurant_id criterion, and either deletes the corresponding restaurant or does nothing.

**Response**

```
{
    "message": "Successfully deleted restaurant!",
    "status": "success"
}
```

**Endpoint**

    DELETE /restaurant/name/<restaurant_name>

This searches the Restaurant relation by the restaurant_name criterion, and either deletes all the corresponding restaurants with the given name or does nothing.

**Response**

```
{
    "message": "Successfully deleted all instances of restaurant!",
    "status": "success"
}
```

**Endpoint**

    POST /restaurant

Creates a new user in the User table given the correct input.

**Input**

|   Name   |  Type  |
|:--------:|:------:|
| restaurant_id | int |   **Required** | 1
| restaurant_name | string |   **Required** | McDonalds

This input must be passed in the form of JSON, as below:

```
{
  "restaurant_id": 1,
  "restaurant_name": "McDonalds"
}
```

**Response**

```
{
    "message": "Created new restaurant!",
    "status": "success"
}
```

## Location

## Serves

## Cuisine

## Photo

## Rating
