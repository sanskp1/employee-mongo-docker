from pymongo import MongoClient
from faker import Faker
import random

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client['company']
employees = db['employees']

# Generate fake data
fake = Faker()
records = []
for _ in range(10000):
    records.append({
        "employee_id": fake.name(),
        "name": fake.name(),
        "age": random.randint(20, 60),
        "city": random.choice(["Pune", "New Delhi", "Mumbai", "Bengaluru"]),
        "salary": random.randint(30000, 150000)
    })

# Insert data into the collection
employees.insert_many(records)
print("Inserted 10,000 employee records!")