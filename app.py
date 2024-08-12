import json
import logging
from flask import Flask, Blueprint, jsonify, request, send_from_directory, render_template
import openai

bp = Blueprint("routes", __name__, static_folder="static", template_folder="static")

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='static')
    app.register_blueprint(bp)
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    # Initialize OpenAI API key (ensure it's stored securely in a real application)
   # openai.api_key = "your-openai-api-key"

    @app.before_first_request
    def init():
        try:
            # Remove any database initialization code
            pass
        except Exception as e:
            logging.exception("Failed to initialize components")
            raise e

    return app

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
    # Process the request here
    return jsonify({"response": "Processed"})

@bp.route("/frontend_settings", methods=["GET"])
def get_frontend_settings():
    try:
        # Return some default settings or dummy data
        return jsonify({
            "auth_enabled": False,
            "feedback_enabled": False,
            "ui": {
                "title": "Chatbot",
                "logo": "",
                "chat_logo": "",
                "chat_title": "Chat with us",
                "chat_description": "Ask us anything",
                "show_share_button": False,
                "show_chat_history_button": False,
            },
            "sanitize_answer": True,
        }), 200
    except Exception as e:
        logging.exception("Exception in /frontend_settings")
        return jsonify({"error": str(e)}), 500

@bp.route('/api/chatbot/sendMessage', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message')
    if not message:
        return jsonify({"error": "Message is required"}), 400
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=150
        )
        reply = response.choices[0].text.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
