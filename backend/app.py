from flask import Flask, jsonify
from flask_cors import CORS
from azure.identity import ClientSecretCredential
from azure.mgmt.costmanagement import CostManagementClient
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Autonomous Cloud Cost Intelligence Backend Running"

@app.route("/cost")
def get_cost():
    try:
        credential = ClientSecretCredential(
            tenant_id=os.environ["AZURE_TENANT_ID"],
            client_id=os.environ["AZURE_CLIENT_ID"],
            client_secret=os.environ["AZURE_CLIENT_SECRET"],
        )

        subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

        cost_client = CostManagementClient(credential)

        query = {
            "type": "ActualCost",
            "timeframe": "MonthToDate",
            "dataset": {
                "granularity": "None",
                "aggregation": {
                    "totalCost": {
                        "name": "PreTaxCost",
                        "function": "Sum"
                    }
                }
            }
        }

        scope = f"/subscriptions/{subscription_id}"

        result = cost_client.query.usage(scope, query)

        amount = result.rows[0][0]

        return jsonify({
            "current_cost": round(amount, 2),
            "predicted_cost": round(amount * 1.1, 2),
            "recommendation": "Monitor high usage resources to reduce cost"
        })

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/auth-test")
def auth_test():
    try:
        credential = ClientSecretCredential(
            tenant_id=os.getenv("AZURE_TENANT_ID"),
            client_id=os.getenv("AZURE_CLIENT_ID"),
            client_secret=os.getenv("AZURE_CLIENT_SECRET")
        )

        credential.get_token("https://management.azure.com/.default")
        return jsonify({"status": "Azure Authentication Successful"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)