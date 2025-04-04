from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def search_orders(question):
    # Recherche naïve par mots-clés dans plusieurs champs
    body = {
        "query": {
            "multi_match": {
                "query": question,
                "fields": [
                    "product_id", "order_date", "customer_id",
                    "model", "category1", "category2", "frame"
                ]
            }
        }
    }
    try:
        res = es.search(index="orders", body=body, size=10)
        return [hit["_source"] for hit in res["hits"]["hits"]]
    except Exception as e:
        return [{"error": str(e)}]
