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

def get_hotel_rooms(q):
    result = []
    cursor = connection.cursor()
    query = """SELECT * FROM "BookingpediaApp_room" where hotel_id = %s"""
    q == f'{q}'
    cursor.execute(query, (q,))
    result = dictfetchall(cursor)
    return result

def get_hotel_rooms_between(q, max, min):
    result = []
    cursor = connection.cursor()
    query = """SELECT * FROM "BookingpediaApp_room" where hotel_id = %s AND price <= %s AND price >= %s"""
    q == f'{q}'
    max == f'{max}'
    min == f'{min}'
    cursor.execute(query, (q, max, min))
    result = dictfetchall(cursor)
    return result

def get_hotel_rooms_max(q, max):
    result = []
    cursor = connection.cursor()
    query = """SELECT * FROM "BookingpediaApp_room" where hotel_id = %s AND price <= %s"""
    q == f'{q}'
    max == f'{max}'
    cursor.execute(query, (q, max,))
    result = dictfetchall(cursor)
    return result

def get_hotel_rooms_min(q, min):
    result = []
    cursor = connection.cursor()
    query = """SELECT * FROM "BookingpediaApp_room" where hotel_id = %s AND price >= %s"""
    q == f'{q}'
    min == f'{min}'
    cursor.execute(query, (q, min,))
    result = dictfetchall(cursor)
    return result

def get_reservations(q):
    result = []
    cursor = connection.cursor()
    query = """ SELECT res.id as id, res.start_date as start_date, res.end_date as end_date, hot.name as name, room.number as number
                FROM "BookingpediaApp_reservation" res
                JOIN "BookingpediaApp_room" as room ON res.room_id = room.id
                JOIN "BookingpediaApp_hotel" as hot ON room.hotel_id = hot.id
                WHERE customer_id =  %s
            """
    q == f'{q}'
    cursor.execute(query, (q,))
    result = cursor.fetchall()
    return result