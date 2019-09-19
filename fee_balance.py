# import python driver for mongodb
import pymongo

# create client to communicate with the server
client = pymongo.MongoClient("mongodb://localhost:27017")

# Select database
Students = client["students"]

# select collection
school_fees = Students["fees"]

# fecth all records
students_fees = school_fees.find({}, {"_id": 0})

print("Students with outstanding fee balances!")
for student in students_fees:
    if student['fee_paid'] < (student['total_fees']/2):
        print(student)
