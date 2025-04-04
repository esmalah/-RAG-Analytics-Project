from flask import Flask, request, render_template
from utils.elasticsearch_client import search_orders

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    question = ""
    if request.method == "POST":
        question = request.form["question"]
        results = search_orders(question)
    return render_template("index.html", question=question, results=results)

if __name__ == "__main__":
    app.run(debug=True)
