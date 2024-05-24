from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "testing endpoint"

@app.route("/hala")
def homes():
    return "rotuing working"

@app.route("/users/<id>")
def getUser(id):
    user_data = {
        "id": id,
        "name": "Jonathan Andujo",
        "email": "jonathan_andujo@outlook.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

@app.route("/users/create", methods=["POST"])
def createUser():
    data = request.get_json()

    return jsonify(data), 201
    

if __name__ == "__main__":
    app.run(debug=True)