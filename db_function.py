import sqlite3

import sqlite3


conn = sqlite3.connect("data/RJDdb.db", check_same_thread=False)

c = conn.cursor()

def add_userdata(first_name, last_name,email, password):
    c.execute("INSERT INTO user(first_name, last_name, email, USER_id, package_id, password) VALUES (?,?,?,?,?,?)", (first_name, last_name, email, 0, 0, password))
    conn.commit()
def login_user(email, password):
    c.execute("SELECT * FROM user WHERE email = ? AND password = ?", (email, password))
    data = c.fetchall()
    return data

def history_package():
    pass

def post_package():
    pass