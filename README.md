<a>
  <img src="https://training.talkpython.fm/static/course_images/eve-and-mongo.png" />
</a>

<h1>Proyecto- Ranking Memes.</h1>


El objetivo principal de este proyecto fué desarrollar una API utilizando Flask de herramienta, integrando dicha API con una base de datos que exportamos a MongoDB vía Pymongo.

<h2>·Ejecución del programa:</h2>

    '/student/create/<name>'
    
Creamos un usuario nuevo, y el sistema nos devolverá un ID generado para este nuevo usuario.
  
    '/student/all'

Nos devolverá el nombre de todos los usuarios de nuestra Base de Datos.

    '/lab/create/<name>'
  
Creamos un nombre de lab nuevo, y el sistema nos regresará un ID generado para este nuevo lab.

    '/lab/<lab-id>/search'
    
 Busca el lab por idd en la base de datos 
  

<h2>·Documentos encontrados:</h2> 

-server.py: que es el fichero principal que nos conecta a nuestro rervidor


-controllerstudent y controllerlab: archivos que ejecutan las funciones de obtencion de data de la api de de Github ,las funciones de insercion de esos datos en Mongo  y las funciones de busqueda de querys .

-Github: contiene las funciones de extraccion de data de la API de Github

-Database: archivo que conecta a la base de datos de Mongodb

  
<h2>·Herramientas utilizadas:</h2>

<a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank">Flask</a> 

<a href="https://api.mongodb.com/python/current/installation.html" target="_blank">Pymongo</a> 

<a href="https:/www.mongodb.com/" target="_blank">MongoDB</a> 


<h2>·Apredizaje: Creación de API's a través de Flask</h2>
