
from app import app
from config import PORT
import controllerstudent 
import controllerlab
from database import db

app.run("0.0.0.0", 
        PORT, debug=True, load_dotenv=False)