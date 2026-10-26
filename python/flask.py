# What is Flask?
# Flask is a lightweight Python web framework used to build web applications and REST APIs.
#  It provides routing, request handling, and response generation, with extensions available for other capabilities.

# What is a REST API?
# REST Stands for the Representational State Transfer Application Programming Interface .
# A REST API lets clients interact with resources over HTTP using methods such as GET, POST, PUT, PATCH, and DELETE.
# Method	Typical purpose
# GET	    Retrieve data
# POST	    Create a resource or initiate an operation
# PUT	    Replace a resource
# PATCH	    Partially update a resource
# DELETE	Delete a resource

# 200 OK — successful request.
# 201 Created — resource created.
# 204 No Content — successful request without a response body.
# 400 Bad Request — invalid client input.
# 401 Unauthorized — authentication is missing or invalid.
# 403 Forbidden — access is not permitted.
# 404 Not Found — resource not found.
# 500 Internal Server Error — unexpected server-side failure.
# 503 Service Unavailable — service temporarily unable to handle requests.

from flask import Flask ,jsonify, request

app = Flask(__name__)

users =[
    {
        "id" : 1, "name" : "subash"
    }
]
@app.get("/users")
def get_users():
    return jsonify(users) ,200

@app.post("/users")
def create_user():
    data = request.get_json(silent=True) or {}

    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    user = {
        "id": len(users) + 1,
        "name": data["name"]
    }

    users.append(user)
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(debug=True)