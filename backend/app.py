from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Autonomous Cloud Cost Intelligence Backend Running"

@app.route("/cost")
def get_cost():
    return jsonify({
        "current_cost": 720,
        "predicted_cost": 850,
        "recommendation": "Stop unused instances to reduce cloud cost"
    })

if __name__ == "__main__":
    app.run(debug=True)
