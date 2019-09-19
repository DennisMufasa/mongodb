# mongodb_intro
Basic concepts of mongodb a NoSQL database that includes installing the database and using a python driver for mongodb to connect and query the database.
## set up
1. Download mongodb server for your operating system from their official page.
2. Install the serve and test for a successful connection
3. Start the server (for me on ubuntu 19 `sudo service mongod start`)
4. Strat your text editor or IDE
5. Create a python virtual environment for me `python3 -m venv env` (If using IDE ignore step 5)
6. Download the python driver for mongodb called PyMongo (for me `python -m pip install pymongo`)
7. Create a python file and run this `import pymongo` code to test successful installation of pymongo if no errors       occur.


## Tasks to accomplish
1. Create a mongodb database and call it students
2. create collections for student personal info
3. create collections for student academic progress
4. create collections for student fee completion 
5. Populate all the collections with documents
6. fetch all student names and their courses
7. fetch all students below 20 years of age
8. fetch all students whose fee balance is more than half the agreed amount
9. fetch all students whose Grade point averages are above 70 for a first class honours