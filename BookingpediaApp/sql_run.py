'''
This file should comprise of functions that generate run
queries and resturn ORM objects. There should be one function for
each object type in our database. The function should set the transaction level,
then run the query provided in the first argument. Then, it should intersect
that first query with the second query and so on. Finally, it should terminate
with a ';'
'''

from django.db import connection

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def get_reserved_rooms():
    result = []
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT * FROM "BookingpediaApp_hotel" JOIN 
                (SELECT id as room_id, number, hotel_id FROM "BookingpediaApp_room" WHERE id IN (SELECT room_id FROM "BookingpediaApp_reservation")) Reserved_room 
            ON id = hotel_id''')
        
        result = dictfetchall(cursor)
    return result

def get_unreserved_rooms():
    result = []
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT * FROM "BookingpediaApp_hotel" JOIN 
                (SELECT id as room_id, number, hotel_id FROM "BookingpediaApp_room" WHERE id NOT IN (SELECT room_id FROM "BookingpediaApp_reservation")) Reserved_room 
            ON id = hotel_id''')
        
        result = dictfetchall(cursor)
    return result

def get_customer_name(q):
    result = []
    cursor = connection.cursor()
    query = """SELECT * FROM "BookingpediaApp_customer" where username LIKE %s"""
    like_val = f'%{q}%'    
    cursor.execute(query, (like_val,))
    result = dictfetchall(cursor)
    return result

def sort_bill_cust_d():
    result = []
    with connection.cursor() as cursor:
        cursor.execute(""" SELECT * FROM "BookingpediaApp_customer" ORDER BY bill DESC """)
        result = dictfetchall(cursor)
    return result

def sort_bill_cust_a():
    result = []
    with connection.cursor() as cursor:
        cursor.execute(""" SELECT * FROM "BookingpediaApp_customer" ORDER BY bill ASC """)
        result = dictfetchall(cursor)
    return result


def get_hotel_name(q):
    result = []
    cursor = connection.cursor()
    query = """SELECT * FROM "BookingpediaApp_hotel" where name LIKE %s"""
    like_val = f'%{q}%'    
    cursor.execute(query, (like_val,))
    result = dictfetchall(cursor)
    return result

def sort_start_date_acs():
    result = []
    with connection.cursor() as cursor:
        cursor.execute("""  SELECT "BookingpediaApp_reservation".id as id ,start_date, end_date, hotel_id, number as room_number, customer_id
                            FROM "BookingpediaApp_reservation" 
                            join "BookingpediaApp_room" on "BookingpediaApp_reservation".room_id = "BookingpediaApp_room".id
                            ORDER BY start_date ASC """)
        result = dictfetchall(cursor)
    return result

def get_item_name(q):
     result = []
     cursor = connection.cursor()
     query = """SELECT * FROM "BookingpediaApp_item" where name LIKE %s"""
     like_val = f'%{q}%'    
     cursor.execute(query, (like_val,))
     result = dictfetchall(cursor)
     return result

def get_item_price(q):
     result = []
     cursor = connection.cursor()
     query = """SELECT * FROM "BookingpediaApp_item" where price = %s"""
     like_val = f'{q}'  
     cursor.execute(query, (like_val,))
     result = dictfetchall(cursor)
     return result

def get_transaction_item(q):
     result = []
     cursor = connection.cursor()
     query = """SELECT "BookingpediaApp_transaction".item_id, "BookingpediaApp_item".name, "BookingpediaApp_item".price, count(*)
                FROM "BookingpediaApp_transaction"
                JOIN "BookingpediaApp_item"
				ON "BookingpediaApp_transaction".item_id = "BookingpediaApp_item".id
                GROUP BY "BookingpediaApp_item".name, "BookingpediaApp_item".id, "BookingpediaApp_transaction".item_id"""
     like_val = f'%{q}%'
     cursor.execute(query, (like_val,))
     result = dictfetchall(cursor)
     return result

def get_transaction_customer(q):
     result = []
     cursor = connection.cursor()
     query = """SELECT customer_id, "BookingpediaApp_customer".username, count(*)
                FROM "BookingpediaApp_transaction"
                JOIN "BookingpediaApp_customer" ON "BookingpediaApp_transaction".customer_id = "BookingpediaApp_customer".id
                GROUP BY "BookingpediaApp_customer".username, customer_id"""
     like_val = f'%{q}%'  
     cursor.execute(query, (like_val,))
     result = dictfetchall(cursor)
     return result
