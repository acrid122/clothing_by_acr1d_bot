from main import *
from KEYBOARD_TYPE_EVENT import *
import sqlite3 as sq
from multipledispatch import dispatch


with sq.connect("users.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY DEFAULT 1,
            email TEXT DEFAULT 0,
            delivery_address TEXT NOT NULL DEFAULT 0,
            phone_number TEXT NOT NULL DEFAULT 0,
            FIO TEXT NOT NULL DEFAULT 0
    )""")
    

#Check in USERS_DB
def checkInUSERS_DB(from_id):
    with sq.connect("users.db") as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        info = cur.execute(f"SELECT user_id FROM users WHERE user_id == {from_id}")
        if info.fetchone() is None:
          return True
        return False


#Insert new user to USERS_DB
def insertUserToUSERS_DB(new_user_id):
    with sq.connect("users.db") as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        cur.execute("INSERT INTO users VALUES (?,?,?,?,?)", (new_user_id,0,0,0,0))                
        for res in cur:
            print(res['user_id'], res['email'])
            

#Update new user in USERS_DB
def updateUserInfoInUSERS_DB(new_user_id, new_email, new_delivery_address, new_phone_number, new_fio):
    with sq.connect("users.db") as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        cur.execute("UPDATE users SET email = '"+ new_email +"' , delivery_address = '"+ new_delivery_address
                    +"', phone_number = '"+ new_phone_number +"', FIO = '" + new_fio + "' WHERE user_id ='" + new_user_id + "' ") 


#Update old user's data in USERS_DB

#Update user email data in USERS_DB
def updateUserEmailDataInUSERS_DB(user_id, new_email):
    with sq.connect("users.db") as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        cur.execute("UPDATE users SET email = '"+ new_email +"' WHERE user_id ='" + user_id + "' ")


#Update user phone_number data in USERS_DB
def updateUserPhoneNumberDataInUSERS_DB(user_id, new_phone_number):
    with sq.connect("users.db") as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        cur.execute("UPDATE users SET phone_number = '"+ new_phone_number +"' WHERE user_id ='" + user_id + "' ")
        

#Update user delivery_address data in USERS_DB
def updateUserDeliveryAddressDataInUSERS_DB(user_id, new_delivery_address):
    with sq.connect("users.db") as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        cur.execute("UPDATE users SET delivery_address = '"+ new_delivery_address +"' WHERE user_id ='" + user_id + "' ")


#Update user FIO data in USERS_DB
def updateUserFioDataInUSERS_DB(user_id, new_FIO):
    with sq.connect("users.db") as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        cur.execute("UPDATE users SET FIO = '"+ new_FIO +"' WHERE user_id ='" + user_id + "' ")


#Get info about user in USERS_DB
def getUserInUSERS_DB(user_id):
    with sq.connect("users.db") as con:
        con.row_factory = sq.Row
        cur = con.cursor()
        cur.execute("SELECT email, delivery_address, phone_number, FIO FROM users WHERE user_id = '" + user_id + "'")
        for rec in cur.fetchall():
            return [rec['email'], rec['delivery_address'], rec['phone_number'], rec['FIO']];