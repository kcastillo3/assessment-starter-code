from flask import request, make_response, jsonify
from config import app, db, api
from models import Project
from flask_restful import Resource

import ipdb

# GET '/projects' which should return a json response with all the projects 
# that are in the database along with the appropriate status code. Do not worry about serialization.

# POST '/projects' which should create a new project with the json in the 
# request and send back the new project in the response body with the appropriate status code. Do not worry about serialization.

    # name = db.Column(db.String)
    # about = db.Column(db.String)
    # phase = db.Column(db.String)
    # link = db.Column(db.String)
    # image = db.Column(db.String)

@app.route('/')
def index():
    return 'Index for Project'

@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    projects_data = [project.to_dict() for project in projects]
    return make_response(jsonify(projects_data), 200)

@app.route('/projects', methods=['POST'])
def projects():
    try:
        data = request.get_json()
        new_project = Project(name=data['name'], about=data['about'], phase=data['phase'], link=data['link'], image=data['image'])
        db.session.add(new_project)
        db.session.commit()
        return make_response(jsonify(new_project.to_dict()), 201)
    except ValueError:
        return make_response(jsonify({'errors':['validation errors']}), 400)

if __name__=='__main__':
    app.run(port=5555, debug=True)

