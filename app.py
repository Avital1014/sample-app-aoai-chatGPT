from flask import Flask, jsonify, request, render_template, send_from_directory

app = Flask(__name__, static_folder='static', template_folder='static')

@app.route("/")
def index():
    return render_template("index.html", title="Chatbot", favicon="favicon.ico")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "favicon.ico")

@app.route("/assets/<path:path>")
def assets(path):
    return send_from_directory("static/assets", path)

@app.route("/conversation", methods=["POST"])
def conversation():
    if not request.is_json:
        return jsonify({"error": "request must be json"}), 415
    request_json = request.get_json()
    return jsonify({"response": "Processed"})

if __name__ == '__main__':
    app.run(debug=True)
