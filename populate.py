import json, random
from datetime import datetime, time, timedelta
from api import db, models

restaurants = json.load(open('restaurants.json', 'rb'))
cuisines = json.load(open('cuisines.json', 'rb'))
users = json.load(open('users.json','rb'))
checkins = json.load(open('checkins.json', 'rb'))

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

# def populate_ratings():
#     Users = db.session.query(models.User).all()
#     Restaurants = db.session.query(models.Restaurant).all()
#     for user in Users:
#         for restaurant in Restaurants:
#             rating_ORM = models.Rating(user_id = user.user_id, restaurant_id = restaurant.restaurant_id, rating=random.gauss(3, 0.75))
#             db.session.add(rating_ORM)
#     db.session.commit()

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

def populate_checkins_and_ratings():
    # generate 30 random checkins today from the first 10 users and the first 10 
    for checkin in checkins["checkins"]:
        checkin = checkin['checkin']
        now = datetime.now()
        midnight = datetime.combine(now.date(), time.min)
        delta = int((now - midnight).total_seconds())
        random_dt = midnight + timedelta(seconds=random.randrange(delta))
        date_time_stamp = random_dt.strftime('%Y-%m-%d %H:%M:%S')
        print(date_time_stamp)
        checkin_ORM = models.Checkins(location_id=checkin["location_id"], user_id=checkin["user_id"], timestamp=date_time_stamp)
        db.session.add(checkin_ORM)

    for x in range(1, 107):
        two_years_ago = datetime.now() - timedelta(days=2*365)
        one_year_ago = datetime.now() - timedelta(days=1*365)
        one_month_ago = datetime.now() - timedelta(days=30)

        # generate 30 visits from 2 years ago to 1 year ago
        for y in range(30):
            delta = int((one_year_ago - two_years_ago).total_seconds())
            random_dt = two_years_ago + timedelta(seconds=random.randrange(delta))
            location_restaurant_id=random.randrange(1,101)
            checkin_ORM = models.Checkins(location_id=location_restaurant_id, user_id=x, timestamp=random_dt.strftime('%Y-%m-%d %H:%M:%S'))
            rating_ORM = models.Rating(user_id = x, restaurant_id = location_restaurant_id, rating=random.gauss(3, 0.75), timestamp=random_dt.strftime('%Y-%m-%d %H:%M:%S'))
            db.session.add(checkin_ORM)
            db.session.add(rating_ORM)
        # generate 15 visits from 1 year ago to 1 month ago
        for y in range(15):
            delta = int((one_month_ago - one_year_ago).total_seconds())
            random_dt = one_year_ago + timedelta(seconds=random.randrange(delta))
            location_restaurant_id=random.randrange(1,101)
            checkin_ORM = models.Checkins(location_id=location_restaurant_id, user_id=x, timestamp=random_dt.strftime('%Y-%m-%d %H:%M:%S'))
            rating_ORM = models.Rating(user_id=x, restaurant_id = location_restaurant_id, rating=random.gauss(3, 0.75), timestamp=random_dt.strftime('%Y-%m-%d %H:%M:%S'))
            db.session.add(checkin_ORM)
            db.session.add(rating_ORM)
        # generate 10 visits from 1 month ago to today
        for y in range(10):
            delta = int((datetime.now() - one_month_ago).total_seconds())
            random_dt = two_years_ago + timedelta(seconds=random.randrange(delta))
            location_restaurant_id=random.randrange(1,101)
            checkin_ORM = models.Checkins(location_id=location_restaurant_id, user_id=x, timestamp=random_dt.strftime('%Y-%m-%d %H:%M:%S'))
            rating_ORM = models.Rating(user_id=x, restaurant_id = location_restaurant_id, rating=random.gauss(3, 0.75), timestamp=random_dt.strftime('%Y-%m-%d %H:%M:%S'))
            db.session.add(checkin_ORM)
            db.session.add(rating_ORM)
    db.session.commit()

populate_cuisines()
populate_restaurants()
populate_users()
# populate_ratings()
populate_checkins_and_ratings()