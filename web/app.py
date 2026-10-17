from flask import Flask, render_template, abort, request
import os


app = Flask(__name__)

@app.route("/<path:name>")
def status_200(name):
    if "~" in name or ".." in name or "//" in name:
        abort(403)
    elif name.endswith(".html") and os.path.isfile("templates/" + name) == True:
        return render_template(name)
    else:
        abort(404)

@app.errorhandler(403)
def error_403(forbidden):
    return render_template("403.html"), 403

@app.route('/')
def hello():
    return "UOCIS docker demo!"

@app.errorhandler(404)
def error_404(not_found):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(port=5000,debug=True,host='0.0.0.0')
