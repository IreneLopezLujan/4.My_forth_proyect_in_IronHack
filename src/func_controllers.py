 
from database import db
from bson.objectid import ObjectId
from bson.errors import InvalidId




def insert_student(student):
    """
    Inserta estudiantes a la base de datos si aún no existen.
    
    """
    
    query = {"username": student["username"]}
    if db["students"].find_one(query):
        return None

    oid = db["students"].insert_one(student).inserted_id
    return str(oid)


def fetch_students(project=None):

    """
    Llama a los estudiantes de la base de datos 
    
    """

    projection = {"_id": 0}
    if project:
        if isinstance(project, list):
            for attr in project:
                projection[attr] = 1
                print(projection[attr])
        else:
            projection[project] = 1

    cur = db["students"].find({}, projection=projection)

    # Check if collection is empty
    if cur.count() == 0:
        return None

    return list(cur)


def insert_pulls(pulls):
    """
    Inserta todas las pulls en la base de datos 
    
    """
    for pull in pulls:
        # Check if pull already in database
        query = {"number": pull["number"]}
        if db["pulls"].find_one(query):
            continue
        
        db["pulls"].insert_one(pull)


def fetch_pulls(lab_name):
    """
    Llama todas las pull request y encuentra en nombre del lab

    """
    cur = db["pulls"].find({"lab": lab_name}, projection={"_id": 0})

    if cur.count() == 0:
        return None

    return list(cur)



def insert_new_lab(labname):
    """
    Inserta un nuevo nombre de lab en la base de datos

    """
    new_lab = {
        "lab_name": labname,
        "lab_name_pull": f"[{labname}]".replace(' ','-')
        }
    result = db.labs.insert_one(new_lab)
    return {"_id": str(result.inserted_id)}


def fetch_lab(project=None):
    """
    Llama todos los labs de la base de datos
    
    """
    projection = {"_id": 0}
    if project:
        if isinstance(project, list):
            for attr in project:
                projection[attr] = 1
        else:
            projection[project] = 1

    cur = db["labs"].find({}, projection=projection)

    if cur.count() == 0:
        return None

    return list(cur)



