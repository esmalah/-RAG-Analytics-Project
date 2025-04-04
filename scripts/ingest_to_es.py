import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# Connexion à Elasticsearch (existant sur localhost:9200)
es = Elasticsearch("http://localhost:9200")

def index_csv_to_es(csv_path, index_name):
    print(f"📥 Indexation de {csv_path} vers l'index '{index_name}'...")
    
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip().str.lower()

    actions = [
        {
            "_index": index_name,
            "_source": row.dropna().to_dict()
        }
        for _, row in df.iterrows()
    ]

    success, _ = bulk(es, actions)
    print(f"✅ {success} documents indexés dans '{index_name}'")

# Indexation des 4 fichiers
index_csv_to_es("../outputs/clean_bikes.csv", "bikes")
index_csv_to_es("../outputs/clean_bikeshops.csv", "bikeshops")
index_csv_to_es("../outputs/clean_customers.csv", "customers")
index_csv_to_es("../outputs/clean_orders.csv", "orders")
