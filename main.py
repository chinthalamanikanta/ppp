from flask import Flask, render_template_string

app = Flask(__name__)

HOME_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 100px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Flask App</h1>
    <p>This is the home page.</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_PAGE)

if __name__ == "__main__":
    app.run(debug=True)
