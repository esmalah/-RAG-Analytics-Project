def extract_filters_from_question(question: str):
    filters = []

    q = question.lower()

    if "carbone" in q or "carbon" in q:
        filters.append({"match": {"frame": "Carbon"}})

    if "aluminium" in q:
        filters.append({"match": {"frame": "Aluminum"}})

    if "route" in q:
        filters.append({"match": {"category1": "Road"}})

    if "montagne" in q or "mountain" in q:
        filters.append({"match": {"category1": "Mountain"}})

    if "triathlon" in q:
        filters.append({"match": {"category2": "Triathalon"}})

    if "client" in q or "acheteur" in q:
        filters.append({"exists": {"field": "customer_id"}})

    return filters
