from flask import Flask
from dotenv import load_dotenv, find_dotenv
import os

# Datos de conexión a Mongodb Atlas
# host = 'cluster0.gf1lwbd.mongodb.net'
# usuario = 'jcgutierrez02'
# passwd = 'Jujuaxr_700'
# bd = 'tienda' 
#

load_dotenv(find_dotenv())
host = os.environ.get("MONGODB_HOST")
usuario = os.environ.get("MONGODB_USUARIO")
passwd = os.environ.get("MONGODB_PASSWORD")
bd = os.environ.get("MONGODB_BD")
        
app = Flask(__name__)

# Para conexiones en la nube se requiere tener instalado el paquete dnspython
# Se ejecuta el comando: py -m pip install pymongo[srv]
app.config['MONGO_URI'] = f'mongodb+srv://{usuario}:{passwd}@{host}/{bd}'