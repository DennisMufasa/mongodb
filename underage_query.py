# import pyhton driver for mongodb
import pymongo

# import datetime library
import datetime

# create client to communicate with the server
client = pymongo.MongoClient("mongodb://localhost:27017")

# select database
Students = client["students"]

# select collecction
info = Students["info"]

# current year
current_year = datetime.datetime.now().year

# restricted age
restricted_age = 25

# legal year of birth
legal_yob = current_year - restricted_age

# query object
# this is an advanced query
# the object tells python to filter students "yob"
# and remove the students with a smaller "yob" and thus older than 25
underage_query = {"yob": {"$gt":legal_yob}}

# query the database using my query object
underage_students = info.find(underage_query)

# display results
for student in underage_students:
    print(student)
