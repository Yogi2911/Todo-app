from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Sample Todo Application</h1>
    <p>Welcome to the application!</p>
    <a href="/login">Login</a>
    """


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin123":
            return """
            <h2>Login Successful</h2>
            <p>Welcome, admin!</p>
            """

        return """
<h2>Login Failed</h2>
<p>Invalid username or password. Please check your credentials and try again.</p>
<a href="/login">Try again</a>
"""

    return """
    <h1>Login</h1>

    <form method="POST">

        <label>Username:</label>
        <input type="text" name="username" required>

        <br><br>

        <label>Password:</label>
        <input type="password" name="password" required>

        <br><br>

        <button type="submit">Login</button>

    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)