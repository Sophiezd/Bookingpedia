'''
This file should comprise of functions that generate run
queries and resturn ORM objects. There should be one function for
each object type in our database. The function should set the transaction level,
then run the query provided in the first argument. Then, it should intersect
that first query with the second query and so on. Finally, it should terminate
with a ';'
'''