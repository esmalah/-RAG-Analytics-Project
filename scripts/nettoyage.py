import pandas as pd
import os

# Chemins
data_path = "../data"
output_path = "../outputs"

# Créer le dossier outputs s’il n'existe pas
os.makedirs(output_path, exist_ok=True)

# Chargement des CSV
bikes = pd.read_csv(f"{data_path}/bikes.csv")
bikeshops = pd.read_csv(f"{data_path}/bikeshops.csv")
customers = pd.read_csv(f"{data_path}/Customers.csv")
orders = pd.read_csv(f"{data_path}/orders.csv")

# Nettoyage de base
def clean_df(df, name):
    print(f"\n--- Nettoyage de {name} ---")
    print("Forme initiale :", df.shape)
    print("Colonnes :", df.columns.tolist())

    # Standardisation des noms de colonnes
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    # Suppression des doublons
    df = df.drop_duplicates()
    
    # Suppression des lignes totalement vides
    df = df.dropna(how='all')

    print("Forme après nettoyage :", df.shape)
    return df

# Appliquer le nettoyage
bikes_clean = clean_df(bikes, "bikes")
bikeshops_clean = clean_df(bikeshops, "bikeshops")
customers_clean = clean_df(customers, "customers")
orders_clean = clean_df(orders, "orders")

# Sauvegarde
bikes_clean.to_csv(f"{output_path}/clean_bikes.csv", index=False)
bikeshops_clean.to_csv(f"{output_path}/clean_bikeshops.csv", index=False)
customers_clean.to_csv(f"{output_path}/clean_customers.csv", index=False)
orders_clean.to_csv(f"{output_path}/clean_orders.csv", index=False)

print("\n Fichiers nettoyés enregistrés dans /outputs/")
