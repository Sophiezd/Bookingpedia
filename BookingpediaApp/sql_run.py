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