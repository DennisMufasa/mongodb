# import python driver for mongodb
import pymongo

# create client to communicate with the server
client = pymongo.MongoClient("mongodb://localhost:27017")

# select database
Student = client['students']

# select collection
academics = Student['academics']

# my query object
# the {"$gt": 70} means greater than 69. This to make sure 70 is inclusive
my_query = {"GPA": {"$gt": 69}}

# fecth and filter records based on the query and ommit student id
first_class_honours_students = academics.find(my_query, {"_id": 0})

# output student records
for i in first_class_honours_students:
    print(i)
