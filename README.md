# 🚴‍♀️ RAG Analytics Project — Plateforme d'analyse intelligente

**Plateforme d’analyse interactive des données de vélos, clients et commandes**, avec ingestion, visualisation, et question-réponse en langage naturel grâce à :
- 🐍 **Python**
- 🔎 **Elasticsearch**
- 📊 **Kibana**
- 🔁 **n8n**
- 🌐 **Flask**

---

## 🗂️ Structure du projet

```
rag-analytics-project/
│
├── app/
│   ├── app.py                # Application Flask principale
│   ├── utils/
│   │   ├── elasticsearch_client.py
│   │   └── keyword_parser.py
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   └── static/
│       └── style.css
│
├── data/                     # Fichiers CSV d'origine
│   ├── bikes.csv
│   ├── bikeshops.csv
│   ├── Customers.csv
│   └── orders.csv
│
├── outputs/                  # Fichiers nettoyés
│   ├── clean_bikes.csv
│   ├── clean_bikeshops.csv
│   ├── clean_customers.csv
│   └── clean_orders.csv
│
├── scripts/
│   ├── ingest_to_es.py       # Script Python d’injection dans Elasticsearch
│   └── nettoyage.py          # Nettoyage des données
│
├── notebooks/                # Analyses exploratoires et tests
│
├── docker/
│   └── docker-compose.yml    # Lancement d’Elasticsearch + Kibana
│
├── requirements.txt          # Dépendances Python
└── README.md                 # Ce fichier
```

---

## ⚙️ Installation rapide

### 1. Cloner le projet

```bash
git clone https://github.com/ton_user/rag-analytics-project.git
cd rag-analytics-project
```

### 2. Lancer les services avec Docker

```bash
cd docker
docker-compose up -d
```
> ⚠ Elasticsearch dispo sur `http://localhost:9200` et Kibana sur `http://localhost:5601`

---

##  Créer et activer un environnement virtuel

```bash
python3 -m venv env
source env/bin/activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 🔁 Ingestion des données dans Elasticsearch

```bash
python scripts/ingest_to_es.py
```

> Ce script injecte les **fichiers `clean_*.csv`** dans leurs index respectifs (`orders`, `customers`, `bikes`, etc.)

---

## 🚀 Lancer l’application Flask

```bash
python app/app.py
```

Accès via [http://localhost:5000](http://localhost:5000)

---

## Exemples de requêtes intelligentes

Pose des questions comme :

- **"Qui sont les clients qui achètent le plus de vélos en carbone ?"**
- **"Commandes en 2012 ?"**
- **"Produits de type route et cadre aluminium ?"**

L'application utilise une **analyse de mots-clés** + `multi_match` Elasticsearch pour répondre.

---

## 📊 Dashboards Kibana

Connecte-toi à [http://localhost:5601](http://localhost:5601)  
Tu peux explorer les index (`orders`, `customers`, etc.) et créer des visualisations.

---

## Automatisation avec n8n

Connecte `n8n` à ta base Elasticsearch pour automatiser :
- ingestion régulière
- envoi de données à une API
- alertes par email



---

## 👤 Auteur

Projet réalisé par **@Groupe2**  

---



