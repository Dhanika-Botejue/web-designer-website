from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html", active_page="home")

@app.route("/about")
def about():
    return render_template("about.html", active_page="about")

@app.route("/projects")
def projects():
    return render_template("projects.html", active_page="projects")

@app.route("/connect")
def connect():
    return render_template("connect.html", active_page="connect")


# Serve images from the existing top-level `images/` directory
@app.route("/images/<path:filename>")
def images(filename: str):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run()