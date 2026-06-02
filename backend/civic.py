from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/complaint", methods=["POST"])
def complaint():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Invalid input. Please send 'text' field."}), 400

    user_input = data["text"].lower()

    if "street light" in user_input:
        response = {
            "department": "Municipal Corporation",
            "complaint": "Street light on Road 5 is broken and needs repair.",
        }

    elif "water" in user_input:
        response = {
            "department": "Water Supply Board",
            "complaint": "Water supply issue reported in the area.",
        }

    else:
        response = {
            "department": "General Grievance Cell",
            "complaint": "Complaint registered successfully.",
        }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
