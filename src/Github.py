import requests
import re
from datetime import datetime
from config import BASE_URL, HEADERS, OWNER, REPO

def fetch_user(username):

    """

    Obtiene los usuarios que se encuentran en datamad0820 de la api de Github.
    
    """

    url = f"{BASE_URL}/users/{username}"
    res = requests.get(url, headers=HEADERS)
    
    # Not found
    if res.status_code == 404:
        return None
    else:
    # Parse student
        data = res.json()
        
        return {
                "name": data["name"],
                "username": username,
                "avatar": data["avatar_url"],
                 }





def filtered(raw_pull):


    """

    Filtra todas las pul que se han obtenido por request y nos da los datos relevantes.
    Tambien opera entre algunos de los datos obtenidos y nos los devuelve
    
    """


    #SACAMOS EL NUMERO DE PULL CON REGEX

    number = int(raw_pull["url"].split("/")[-1])

    #SACAMOS EL LAB DE TITLE CON REGEX

    title = raw_pull["title"]
    lab = re.search(r"\w+(-\w+)+", title)
    if lab:
        lab = lab.group()
    else: # invalid title format
        lab= None

    #SACAMOS EL AUTOR: YA SEA PORQUE SE ENCUENTRA CON @ O PORQUE SE ENCUENTRA EN EL BODY DE LOS COMENTARIOS UN JOIN
    #LO PRIMERO LO HACEMOS CON REGEX, Y LO SEGUNDO TENEMOS QUE HACER UNA REQUEST A LOS COMENTARIOS Y ACCEDER AL BODY 
    #AHÍ BUSCAR SI HAY UN JOIN EN CUYO CASO COGEMOS EL USUARIO.

    authors = []
    authors.append(raw_pull["user"]["login"])
    if len(title.split()) >= 5: # additional authors

        if "@" in raw_pull["body"]:
            additional = re.findall(r"@\w+", raw_pull["body"])
            additional = [s.replace("@", "") for s in additional]

        else:
            res = requests.get(raw_pull["comments_url"], headers=HEADERS)
            comments = res.json()
            additional = []
            for comment in comments:
                if comment["body"] == "join":
                    additional.append(comment["user"]["login"])


        authors.extend(additional)

    #BUSCAMOS EL ESTADO DE LA PULL Y SI ESTÁ CERRADA ENTONCES COGEMOS LA FECHA EN QUE SE CERRO

    state = raw_pull["state"]

    #--------------->ERROR al juntar codigo de memes y formulas
    # en grade_times(line 103) y en memes (line 120)----->local variable before assigment.




    #if state == "closed":
        #closed_date= raw_pull["closed_at"][:-1] #sacamos la fecha que se cerró
        #closed=closed_date[:10]+str(" ")+closed_date[-8:]
        #fecha_format1= datetime.strptime(closed, "%Y-%m-%d %H:%M:%S")




        #url = f"{raw_pull['pull_request']['url']}/commits"
        #res = requests.get(url, headers=HEADERS)
        #last_date = res.json()[-1]["commit"]["author"]["date"][:-1]
        #last=last_date[:10]+str(" ")+last_date[-8:]
        #fecha_format2 = datetime.strptime(last, "%Y-%m-%d %H:%M:%S")
       # if closed!='open' and last!=None:
            #grade_time = round((fecha_format1 - fecha_format2).total_seconds() / 3600, 2)
       # else:
            #grade_time = None


    #else:
        #closed='open'
        #last=None


    #memes = []
  
    #img_re = re.compile(r"https://user-images[\S][^()]+")
   
    
    # Get memes of instructor
    #res = requests.get(raw_pull["comments_url"], headers=HEADERS)
    #comments = res.json()
    #for comment in comments:
        #memes=[img_re.findall(comment["body"])[-1][i] for i in range(len(comments)) if comment["user"]["login"] in ["agalvezcorell", "ferrero-felipe", "WHYTEWYLL"]]
            


    return {
            "number": number,
            "lab": lab,
            "authors": authors,
            "state": state,
            #"grade_time": grade_time, 
            #"memes": memes
            }


def fetch_pulls(username):


    """
    Obtiene todas las pull request de los estudiantes de datamad0820 de 
    la API de Github.
    
    """

    url = f"{BASE_URL}/search/issues"
    params = {
                "q": f"repo:{OWNER}/{REPO} is:pr involves:{username}",
                "per_page": 100
                }
    res = requests.get(url, headers=HEADERS, params=params)
    data = res.json()

    pulls = []
   
    for raw_pull in data["items"]:
        open_pulls = sum([True for raw_pull in data["items"] if ["state"] == "open"])
        closed_pulls = len(data["items"]) - open_pulls
        completeness = round(closed_pulls/len(data["items"])*100, 2)
        metricas={'open_pulls':open_pulls,
                    'closed_pulls':closed_pulls,
                 'completeness':completeness  }
        pull = filtered(raw_pull)
        pull.update(metricas)
        pulls.append(pull)
   

    return pulls


