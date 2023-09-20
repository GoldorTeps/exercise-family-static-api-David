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

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }

    return jsonify(members), 200

@app.route ('/member', methods= ['POST'])
def add_member (): 
    member = request.json
    jackson_family.add_member (member)
    return jsonify(), 200

@app.route ('/member/<int:member_id>', methods = ['DELETE'])
def delete_member (id): 
    jackson_family.delete_member (id)
    return jsonify ({"eliminado": True}), 200

@app.route ('/member/<int:id>', methods =['PUT'] )
def update_family_member (id): 
    new_member = request.json
    updated_member = jackson_family.update_member (id, new_member)
    if not updated_member:
        return jsonify ({"msg": "No se encontro al usuario"}), 400
    return jsonify ({"done": "Miembro creado"})

@app.route ('/member/<int:id>', methods = {'GET'})
def get_member (id):
    member = jackson_family.get_member (id)
    return jsonify (member), 200    

jackson_family.add_member ({
    "name": "John",
    "age": 33,
    "luckyNumbers": [7, 13, 22]},
    )
jackson_family.add_member ({
    "name": "Jane",
    "age": 35,
    "luckyNumbers": [10,14,3]},
    )
jackson_family.add_member ({            
    "name": "Jimmy ",
    "age": 5,
    "luckyNumbers": [1]},
)

jackson_family.get_all_members ()


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
