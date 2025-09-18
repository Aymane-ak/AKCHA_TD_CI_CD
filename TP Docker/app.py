from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à MongoDB (adapter le nom du service si nécessaire)
client = MongoClient("mongodb://mongo:27017/")

db = client["testdb"]
collection = db["messages"]

@app.route("/")
def hello():
    # Insertion d’un document
    collection.insert_one({"message": "Hello from Flask & Aymane!"})

    # Lecture du dernier message
    last_msg = collection.find().sort("_id", -1).limit(1)[0]["message"]
    return f"Message enregistré et lu depuis MongoDB : {last_msg}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
