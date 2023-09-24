"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")
jackson_family.add_member({"id":jackson_family._generateId(),"first_name":"John","last_name":"Jackson","age":33,"lucky_numbers":[7,13,22]})
jackson_family.add_member({"id":jackson_family._generateId(),"first_name":"Jane","last_name":"Jackson","age":35,"lucky_numbers":[10,14,3]})
jackson_family.add_member({"id":jackson_family._generateId(),"first_name":"Jimmy","last_name":"Jackson","age":5,"lucky_numbers":[1]})

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(member_id)
    if member == "Couldn't get any member since id doesn't exist":
        return jsonify(member), 404
    return jsonify(member), 200

@app.route("/member", methods = ["POST"])
def add_member():
    body = request.get_json()
    if "first_name" in body.keys() and body["first_name"] != "" and type(body["first_name"]) == str and "last_name" in body.keys() and body["last_name"] != "" and type(body["last_name"]) == str and "age" in body.keys() and body["age"] != "" and "lucky_numbers" in body.keys() and body["lucky_numbers"] != [] and type(body["lucky_numbers"]) == list:
        id = jackson_family._generateId()
        first_name = body["first_name"].capitalize()
        last_name = body["last_name"].capitalize()
        age = body["age"]
        lucky_numbers = body["lucky_numbers"]
        if "id" in body.keys() and body["id"] != "":
            id = body["id"]
            try:
                id = int(id)
                if id < 0:
                    return jsonify("Id must be a positive integer"), 400
            except:
                return jsonify("Id must be an integer number"), 400
        try:
            age = int(age)
            if age < 0:
                return jsonify("Age must be a positive integer"), 400
        except:
            return jsonify("Age must be an integer number"), 400
        jackson_family.add_member({"id":id,"first_name":first_name,"last_name":last_name,"age":age,"lucky_numbers":lucky_numbers})
        return jsonify(f"Member {first_name} added succesfully"), 200
    return jsonify("Parameters missing"), 400

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.delete_member(member_id)
    if member == "Couldn't delete any member since id doesn't exist":
        return jsonify(member), 404
    return jsonify(member), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
