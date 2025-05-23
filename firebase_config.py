import pyrebase

firebase_config = {
    "apiKey": "AIzaSyB3wkpzQmDg6NjgUrVwguN9S5sCHZPh90Y",
    "authDomain": "recanto-f3843.firebaseapp.com",
    "databaseURL": "https://recanto-f3843-default-rtdb.firebaseio.com",
    "projectId": "recanto-f3843",
    "storageBucket": "recanto-f3843.appspot.com",  # Corrigido
    "messagingSenderId": "484366194193",
    "appId": "1:484366194193:web:105895bef48642637743b0"
}

firebase = pyrebase.initialize_app(firebase_config)

auth = firebase.auth()
db = firebase.database()
