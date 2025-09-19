# TP Optimisation Docker

## 🎯 Objectif

L’objectif de ce TP est d’optimiser le `Dockerfile` d’une application Node.js afin de :

* Réduire la taille de l’image Docker
* Améliorer la reproductibilité et la sécurité
* Mettre en place de bonnes pratiques de conteneurisation
* Documenter les impacts de chaque optimisation

---

## 🏗️ Étapes d’optimisation

### 🔹 Baseline (Step0)

* Dockerfile initial
* `FROM node:latest`
* Copie directe de `node_modules` depuis l’hôte
* `npm install` après copie du projet complet
* Exécution en root
* DevDependencies incluses

**Problèmes :** image lourde, non reproductible, manque de sécurité.

### 🔹 Step1 : Fixer la version Node

* Passage à `FROM node:20-alpine` pour plus de stabilité
* Exposition d’un seul port principal

**Impact :** Stabilité, port unique, suppression des dépendances inutiles.

### 🔹 Step2 : Optimiser le cache Docker

* Séparer `COPY package*.json ./` et `COPY . .`

**Impact :** Build plus rapide et reproductible, suppression d’un dossier lourd inutile.

### 🔹 Step3 : Sécurité et optimisation

* `npm ci --omit=dev` pour dépendances production uniquement
* `NODE_ENV=production`
* Utilisation de `USER node`

**Impact :** Réduction de la taille, image sécurisée, dépendances production only.

### 🔹 Step4 : Multi-stage build

* Étape build : installation complète
* Étape finale : copie du code et des dépendances prod uniquement

**Impact :** Image finale minimale, build rapide, sécurité améliorée.

---

## 📊 Progression des tailles et temps de build

### Taille des images

```
Step0  [■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 1,73 GB
Step1  [■■■■■■■■■■] 318 MB
Step2  [■■■■■■■] 230 MB
Step3  [■■■■■] 214 MB
Step4  [■■■■] 210 MB
```

### Temps de build

```
Step0  [■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 67 s
Step1  [■■■] 17 s
Step2  [■■■■] 21 s
Step3  [■■] 12,5 s
Step4  [■] 6,6 s
```

---

## 📋 Progression des étapes et corrections

| Étape | Correction effectuée                                                    | Taille de l'image | Objectif / Impact                                                                                                                   |
| ----- | ----------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Step0 | Baseline (Dockerfile initial)                                           | 1,73 GB           | Image initiale avec mauvaises pratiques : `FROM node:latest`, copie de `node_modules`, exécution en root, devDependencies incluses. |
| Step1 | Fixer la version Node (`FROM node:20-alpine`)                           | 318 MB            | Stabilité : version Node précise, port unique, suppression des dépendances inutiles.                                                |
| Step2 | Optimisation cache Docker (`COPY package*.json` avant `COPY .`)         | 230 MB            | Build plus rapide, image plus propre, Docker utilise le cache efficacement, suppression d’un dossier lourd inutile.                 |
| Step3 | Passage à Alpine + npm ci --omit=dev + USER node + NODE\_ENV=production | 214 MB            | Réduction de taille, image sécurisée, dépendances production only, build reproductible.                                             |
| Step4 | Multi-stage build : copier uniquement le nécessaire                     | 210 MB            | Image finale minimale et propre, dépendances prod only, build rapide, sécurité améliorée.                                           |

---

## ⚙️ Commandes utiles

### Construire chaque étape

```bash
docker build --no-cache -t tp-node:step0 ./tpdockeroptimisation
docker build --no-cache -t tp-node:step1 ./tpdockeroptimisation
docker build --no-cache -t tp-node:step2 ./tpdockeroptimisation
docker build --no-cache -t tp-node:step3 ./tpdockeroptimisation
docker build --no-cache -t tp-node:step4 ./tpdockeroptimisation
```

### Vérifier les tailles

```bash
docker images tp-node:step0
docker images tp-node:step1
docker images tp-node:step2
docker images tp-node:step3
docker images tp-node:step4
```

### Nettoyer les caches Docker

```bash
docker builder prune
```

---

## 💡 Conclusion

* Chaque étape a permis de réduire la taille et améliorer la sécurité/reproductibilité
* La taille est passée de **1,73 GB → 210 MB**
* Les bonnes pratiques Docker appliquées :

  * Version Node fixe
  * Cache optimisé
  * Dépendances production uniquement
  * Utilisateur non-root
  * Multi-stage build
