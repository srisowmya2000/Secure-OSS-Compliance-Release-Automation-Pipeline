from flask import Flask, jsonify, request
app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"ok": True})

@app.get("/hello")
def hello():
    name = request.args.get("name", "world")
    return jsonify({"msg": f"hello, {name}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
