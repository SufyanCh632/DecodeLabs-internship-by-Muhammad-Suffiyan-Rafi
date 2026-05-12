from flask import Flask, render_template_string, request
import random
import string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Random Password Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
            width: 350px;
            text-align: center;
        }

        input {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        button {
            background: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background: #0056b3;
        }

        .password {
            margin-top: 20px;
            font-size: 18px;
            color: green;
            word-wrap: break-word;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Random Password Generator</h2>

    <form method="POST">
        <input type="number" name="length" placeholder="Enter password length" required>
        <br>
        <button type="submit">Generate Password</button>
    </form>

    {% if password %}
        <div class="password">
            <strong>Password:</strong><br>
            {{ password }}
        </div>
    {% endif %}

</div>

</body>
</html>
'''

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@app.route('/', methods=['GET', 'POST'])
def home():
    password = None

    if request.method == 'POST':
        length = int(request.form['length'])
        password = generate_password(length)

    return render_template_string(HTML_TEMPLATE, password=password)


if __name__ == '__main__':
    app.run(debug=True)