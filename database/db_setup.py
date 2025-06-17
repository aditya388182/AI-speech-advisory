# db_setup.py

import firebase_admin
from firebase_admin import credentials, firestore

# Load credentials and initialize Firebase app
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()