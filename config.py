from flask import Flask

# Datos de conexión a Mongodb Atlas
host = 'cluster0.gf1lwbd.mongodb.net'
usuario = 'jcgutierrez02'
passwd = 'Jujuaxr_700'
bd = 'tienda' 
        
app = Flask(__name__)

# Para conexiones en la nube se requiere tener instalado el paquete dnspython
# Se ejecuta el comando: py -m pip install pymongo[srv]
app.config['MONGO_URI'] = f'mongodb+srv://{usuario}:{passwd}@{host}/{bd}'