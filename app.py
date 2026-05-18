from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <h1>Hybrid ECS Deployment</h1>
    <h2>Running Successfully!</h2>
    <p>Container Hostname: {hostname}</p>
    """

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)