from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/texts")
def list_texts():
    base = "texts"
    files = []
    for name in os.listdir(base):
        path = os.path.join(base, name)
        if os.path.isfile(path):
            with open(path) as f:
                files.append({"name": name, "content": f.read()})
    return jsonify(files)

@app.route("/")
def index():
    return "Dev Spaces demo – reading text files from repo"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
