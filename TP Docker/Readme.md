# TP Docker & Flask/MongoDB

## Objectif du TP

L’objectif de ce TP est de se familiariser avec :

- L’installation et la vérification de Docker sur la machine.
- La manipulation de conteneurs simples (`hello-world`, `nginx`).
- L’installation de Python et de ses dépendances (Flask, pip).
- La construction et l’exécution d’une application Flask dans un conteneur.
- La mise en place d’une base de données MongoDB avec Docker Compose.
- La connexion de l’application Flask à MongoDB et la vérification des données.
- La résolution des erreurs courantes rencontrées lors du build ou de l’exécution.

---

## Installation de Docker

```
# Vérifier Docker
docker --version
# Exemple de sortie :
Docker version 24.0.0, build abc123
```

---

## Tester Docker avec Hello World

```
docker pull hello-world
# Pull complet

docker run hello-world
# Hello from Docker!
# This message shows that your installation appears to be working correctly.

docker ps
# CONTAINER ID   IMAGE           STATUS
# 123abc         hello-world     Exited (0) 5 seconds ago

docker ps -a
# Liste tous les conteneurs, même arrêtés
```

---

## Création d’un serveur web Nginx

```
docker pull nginx
# Téléchargement de l'image officielle

docker run -d -p 8080:80 --name mon-nginx nginx
# Lancement en arrière-plan, accessible sur http://localhost:8080

docker ps
# CONTAINER ID   IMAGE   PORTS           NAMES
# xyz789         nginx   0.0.0.0:8080->80/tcp   mon-nginx

docker stop mon-nginx
docker rm mon-nginx
```

---

## Déploiement d’une application Python Flask

### Installation Python et pip

```
pip install flask
pip3 --version
python --version
# Python 3.12.0
```

### Installation via Winget (Windows)

```
winget install -e --id Python.Python.3.12 --source winget --accept-package-agreements --accept-source-agreements
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
python --version
# Python 3.12.0
```

---

## Construire et lancer l’image Flask

```
docker build -t hello-flask .
# [build output...]

docker run -p 5000:5000 hello-flask
# Flask app running on http://0.0.0.0:5000/
```

### Tester l’application

```
curl http://localhost:5000/
# Message attendu : Hello, World! Docker test
```

---

## Déploiement Flask + MongoDB avec Docker Compose

```
docker-compose up --build
# Construction et lancement des services Flask et MongoDB
```

### Vérifier que les conteneurs tournent

```
docker ps
# CONTAINER ID   IMAGE             PORTS                    NAMES
# a1b2c3        td1-flask-app     0.0.0.0:5000->5000/tcp   flask-app
# d4e5f6        mongo:6.0         0.0.0.0:27017->27017/tcp mongo
```

---

### Accéder aux conteneurs pour debug

```
docker exec -it flask-app /bin/sh
# Entrée dans le conteneur Flask

docker exec -it mongo mongosh
# Connexion au shell MongoDB
```

### Vérifier la base MongoDB

```
use testdb
db.messages.find()
# { "message": "Hello from Flask & Aymane!" }
# { "message": "Another test message" }
```

---

## Difficultés rencontrées

```
- J’avais installé Python mais oublié de rebuild l’image Docker → conteneur plantait.
- Solution : rebuild complet
  docker build --no-cache -t td1-flask-app .
```

---

## Résumé des commandes Docker

```
docker build -t <nom> .                # Construire une image
docker run -p <port_host>:<port_container> <image>  # Lancer un conteneur
docker ps                               # Lister les conteneurs actifs
docker ps -a                            # Lister tous les conteneurs
docker rm <container_id>                # Supprimer un conteneur
docker rmi <image>                      # Supprimer une image
docker-compose up --build               # Lancer tous les services définis dans docker-compose.yml
docker exec -it <container> /bin/sh     # Entrer dans un conteneur pour debug
```
