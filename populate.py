import json
import random
from api import db, models

restaurants = json.load(open('restaurants.json', 'rb'))
cuisines = json.load(open('cuisines.json', 'rb'))
users = json.load(open('users.json','rb'))

def populate_cuisines():
    for cuisine in cuisines["cuisines"]:
        cuisine_ORM = models.Cuisine(cuisine_name = cuisine["cuisine"]["cuisine_name"])
        db.session.add(cuisine_ORM)
    db.session.commit()

def populate_users():
    for user in users["users"]:
        user_ORM = models.User(email=user["email"], username=user["username"], password=user["password"], name=user["name"], latitude=user["latitude"], longitude=user["longitude"])
        db.session.add(user_ORM)
    db.session.commit()

def populate_ratings():
    Users = db.session.query(models.User).all()
    Restaurants = db.session.query(models.Restaurant).all()
    for user in Users:
        for restaurant in Restaurants:
            rating_ORM = models.Rating(user_id = user.user_id, restaurant_id = restaurant.restaurant_id, rating=random.gauss(3, 0.75))
            db.session.add(rating_ORM)
    db.session.commit()

def populate_restaurants():
    for restaurant in restaurants["restaurants"]:
        curr_res = restaurant["restaurant"]
        res_ORM = models.Restaurant(restaurant_name = curr_res["name"])
        db.session.add(res_ORM)
        db.session.flush()
        loc_ORM = models.Location(restaurant_id = res_ORM.restaurant_id, address=curr_res["location"]["address"], zipcode=curr_res["location"]["zipcode"], city=curr_res["location"]["locality"], country="USA", latitude=float(curr_res["location"]["latitude"]), longitude=float(curr_res["location"]["longitude"]))
        db.session.add(loc_ORM)
        cuisine_str = curr_res["cuisines"]
        cuisines_list = [x.strip() for x in cuisine_str.split(',')]
        for cuisine in cuisines_list:
            cuisine_ORM = db.session.query(models.Cuisine).filter(models.Cuisine.cuisine_name == cuisine)
            if cuisine_ORM.count() >= 1:
                serve_ORM = models.Serves(restaurant_id=res_ORM.restaurant_id, cuisine_id = cuisine_ORM[0].cuisine_id)
                db.session.add(serve_ORM)
    db.session.commit()

populate_cuisines()
populate_restaurants()
populate_users()
populate_ratings()
