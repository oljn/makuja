import db

def add_restaurant(restaurant_name, restaurant_address, restaurant_description):
    sql = "INSERT INTO restaurants (restaurant_name, restaurant_address, restaurant_description) VALUES (?, ?, ?)"
    db.execute(sql, [restaurant_name, restaurant_address, restaurant_description])

def get_restaurants():
    sql = "SELECT id, restaurant_name FROM restaurants ORDER BY id DESC"
    return db.query(sql)

def get_restaurant(restaurant_id):
    sql = "SELECT restaurants.restaurant_name, restaurants.restaurant_address, restaurants.restaurant_description FROM restaurants WHERE restaurants.id = ?"
    return db.query(sql, [restaurant_id])[0]