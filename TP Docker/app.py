from flask import Flask

# Création de l'application Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    # Lancement du serveur en mode debug
    app.run(debug=True)
