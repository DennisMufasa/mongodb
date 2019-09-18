# import the python driver for mongodb
import pymongo

# import students data
from data import *

# create client
client = pymongo.MongoClient("mongodb://localhost:27017")

# create students database
Students = client["students"]

# create required collections
personal_info = Students["info"]
academics = Students["academics"]
school_fees = Students["fees"]

# populate the collections with documents
insert_personal_info = personal_info.insert_many(students_personal_info)
insert_academic_details = academics.insert_many(students_academics_details)
insert_fees_details = school_fees.insert_many(students_fees_details)

print("personal details ids - ",insert_personal_info.inserted_ids)
print("academics details ids - ",insert_academic_details.inserted_ids)
print("fees details id - ",insert_fees_details.inserted_ids)

