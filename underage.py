# import python driver for mongodb
import pymongo

# import datetime
import datetime

# create client to communicate with the database
client = pymongo.MongoClient("mongodb://localhost:27017")

# select database
Students = client["students"]

# select collection
info = Students["info"]

# current year
current_year = datetime.datetime.now().year

# fetch all students
students = info.find()

print("The Following are below age 25")
# use a for loop to determine whose age is below 25
for student in students:
    if (current_year - int(student['yob'])) < 25:
        print("name - {}\n year of birth: {}".format(student['name'], student['yob']))
