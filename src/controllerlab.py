from database import db
from flask import Flask,request
from func_controllers import fetch_students,fetch_lab,fetch_pulls,insert_new_lab
from app import app
from bson.json_util import dumps
import json


@app.route("/lab/create/", defaults = {"lab_name": None})
@app.route("/lab/create/<lab_name>")
def create_lab(lab_name):
    """

    Adjunta un lab a la base de datos 
    
    """

    inserted  = insert_new_lab(lab_name)

    if inserted:
        return {
                "status": "OK",
                #"msg": f"Lab {pulls['lab']} added succesfully.",  #¡¡No se poque no ba si yo tengo una base de datos llamada asi!!
                "lab_id": inserted
                }

    else:
        return {
                    "status": "Conflict",
                    #"msg": f"Lab {pulls['lab']} already in database.", #aquí igual
                }, 409

@app.route("/lab/<lab_id>/search")
def search_lab(lab_id):

    """

    Recibiendo como input un id devuelve el nombre del lab 
    
    """
  
    lab = fetch_lab(lab_id)
    if not lab:
        return {
                "status": "Not found",
                 "msg": "Enter a valid lab id."
             }, 404
    else:
        return {
                "status": "OK",
                "msg": f"{lab['name']} retrieved successfully.",
                "analysis": lab,
                }

#tengo  analisis hechos en controller student, me falta implementar los memes para finalizar los ultimos endpoints



    
    
    
