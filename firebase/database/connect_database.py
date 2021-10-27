import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://wykopanalysis-default-rtdb.europe-west1.firebasedatabase.app/"
})

ref = db.reference('Data')
print(ref.get())
