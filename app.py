from flask import Flask, Blueprint, jsonify, request, render_template, send_from_directory

bp = Blueprint("routes", __name__, static_folder="static", template_folder="static")

@bp.route("/")
def index():
    return render_template("index.html", title="Chatbot", favicon="favicon.ico")

@bp.route("/favicon.ico")
def favicon():
    return send_from_directory("static", "favicon.ico")

@bp.route("/assets/<path:path>")
def assets(path):
    return send_from_directory("static/assets", path)

@bp.route("/conversation", methods=["POST"])
def conversation():
    if not request.is_json:
        return jsonify({"error": "request must be json"}), 415
    request_json = request.get_json()
    return jsonify({"response": "Processed"})

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='static')
    app.register_blueprint(bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
