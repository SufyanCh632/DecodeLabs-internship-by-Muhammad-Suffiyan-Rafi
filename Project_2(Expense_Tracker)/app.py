from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML Template
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Expense Tracker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 40px;
        }

        .container {
            background: white;
            padding: 20px;
            max-width: 400px;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }

        h1 {
            text-align: center;
        }

        input[type="number"] {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
        }

        button {
            width: 100%;
            padding: 10px;
            margin-top: 15px;
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }

        button:hover {
            background-color: #0056b3;
        }

        .total {
            margin-top: 20px;
            font-size: 20px;
            text-align: center;
            color: green;
        }

        ul {
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Expense Tracker</h1>

    <form method="POST">
        <input type="number" step="0.01" name="expense" placeholder="Enter expense amount" required>
        <button type="submit">Add Expense</button>
    </form>

    <div class="total">
        Total Spent: Rs. {{ total }}
    </div>

    <ul>
        {% for item in expenses %}
            <li>Rs. {{ item }}</li>
        {% endfor %}
    </ul>
</div>

</body>
</html>
"""

# Store expenses
expenses = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        expense = float(request.form["expense"])
        expenses.append(expense)

    total = sum(expenses)

    return render_template_string(
        HTML,
        total=total,
        expenses=expenses
    )

if __name__ == "__main__":
    app.run(debug=True)