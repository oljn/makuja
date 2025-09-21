import db

def add_restaurant(restaurant_name, restaurant_address, restaurant_description):
    sql = "INSERT INTO restaurants (restaurant_name, restaurant_address, restaurant_description) VALUES (?, ?, ?)"
    db.execute(sql, [restaurant_name, restaurant_address, restaurant_description])