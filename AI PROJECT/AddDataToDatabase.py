import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
   'databaseURL':"enter url of firebase here"
})


ref = db.reference('Students')
data = {
    "852741":
        {
            "name": "Emly Blunt",
            "Major": "Economics",
            "starting_year": 2018,
            "total_attendance": 12,
            "standing": "Bad",
            "Year": 2,
            "last_attendance_time": "2023-11-12 00:54:34"

        },
    "963852":
        {
            "name": "Elon musk",
            "Major": "Physics",
            "starting_year": 2014,
            "total_attendance": 14,
            "standing": "Good",
            "Year": 2,
            "last_attendance_time": "2023-11-12 00:54:34"

        },
    "12305835":
        {
            "name": "Rishu Kumar Singh",
            "Major": "CSE",
            "starting_year": 2022,
            "total_attendance": 100,
            "standing": "Good",
            "Year": 4,
            "last_attendance_time": "2023-11-12 00:54:34"

        },
    "12305841":
        {
            "name": "Ishant Divedi",
            "Major": "Sports",
            "starting_year": 2020,
            "total_attendance": 75,
            "standing": "Good",
            "Year": 3,
            "last_attendance_time": "2023-11-12 00:54:34"

        }
}

for key, value in data.items():
    ref.child(key).set(value)