# impoert the python driver for mongodb
import pymongo

# create client
client = pymongo.MongoClient("mongodb://localhost:27017")

# select database
Students = client['students']

# select collection
info = Students['info']

# print all students name and course
details = info.find({}, {"_id":0, "yob": 0})

for student in details:
    print("Name - {}\ncourse - {}\n".format(student["name"], student["course"]))
