from flask import Flask, request

app = Flask(__name__)

# Add methods=["GET", "POST"] right here
@app.route("/", methods=["GET", "POST"])
def home():
    # If GitHub is sending data, it will be a POST request
    if request.method == "POST":
        print("Webhook received successfully from GitHub!")
        return "Webhook Received!", 200
        
    # If you open it in your browser, it's a GET request
    return "Jenkins CI/CD Demo App Running Successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)