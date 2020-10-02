
from flask import Flask,request
from Github import fetch_user,fetch_pulls
from func_controllers import insert_student, insert_pulls,fetch_students
from app import app
from bson.json_util import dumps
import json
from database import db

@app.route("/")
def welcome_page():

    """
    Da la bienvenidaa a mi app

    """

    return {
        "status": "OK",
        "msg": "Welcome to the-ranking-Irene!"
    }




@app.route("/student/create/", defaults = {"studentname": None})
@app.route("/student/create/<student_name>")
def create_student(student_name):

    """
    Adjunta un estudiante a la base de datos
    
    """
  
    student = fetch_user(student_name)
    inserted_id = insert_student(student) 
    pulls = fetch_pulls(student_name)
    insert_pulls(pulls)

    if inserted_id:
        return {
                "status": "OK",
                "msg": f"Student {student['username']} added succesfully.",
                "student_id": inserted_id
                }

    else:
        return {
            "status": "Conflict",
            "msg": f"Student {student['username']} already in database.",
        }, 409

'''
---------->la collection pulls se vería tal que así :

    [{'number': 665,
  'lab': 'lab-supervised-learning-feature-extraction',
  'authors': ['IreneLopezLujan'],
  'state': 'open',
  'open_pulls': 0,
  'closed_pulls': 31,
  'completeness': 100.0},
  ......,
  .....,


---------->la coleccion student se vería tal que así:
{'name': None,
 'username': 'IreneLopezLujan',
 'avatar': 'https://avatars1.githubusercontent.com/u/65113163?v=4'}

'''

@app.route("/student/all")
def list_students():

    """

    Lista los estudiantes de la base de datos
    
    """

    students = fetch_students()
    if not students:
        return {
                "status": "Not found",
                "msg": "No students in database.",
                }, 404

    else:    
        return {
                "status": "OK",
                "msg": "Students retrieved successfuly.",
                "students": students,
                }


    
    
