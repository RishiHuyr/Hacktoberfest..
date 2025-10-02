from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
QUOTES = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "Simplicity is the soul of efficiency."
]

TEMPLATE = """
<!doctype html>
<title>Quotes</title>
<h1>Quotes</h1>
<ul>
  {% for q in quotes %}
    <li>{{ q }}</li>
  {% endfor %}
</ul>
<form method="post" action="{{ url_for('add') }}">
  <input name="quote" placeholder="Add quote" required>
  <button>Add</button>
</form>
"""

@app.route("/")
def home():
    return render_template_string(TEMPLATE, quotes=QUOTES)

@app.route("/add", methods=["POST"])
def add():
    QUOTES.append(request.form["quote"])
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
