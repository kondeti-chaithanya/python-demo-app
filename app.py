from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Jenkins CI/CD Demo App Running Successfully!"

# Add this new route to catch the GitHub Webhook
@app.route("/github-webhook/", methods=["POST"])
def github_webhook():
    print("Webhook received successfully from GitHub!")
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)