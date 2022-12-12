from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user_name'
app.config['MYSQL_PASSWORD'] = 'user_password'
app.config['MYSQL_DB'] = "database_name"

mysql = MySQL(app)


# Funktionsname kann anders heißen
@app.route("/")
def start():
    return "start message"


# Routen- und Funktionsname kann anders heißen
# methods=["GET"] muss angegeben werden, wenn man als client Daten von der FlaskAPI haben will
@app.route("/get", methods=['GET'])
def get():
    # TODO: Code zum Holen der Daten aus Datenbank (sqlLite, mySQL, ...)
    data = []
    return jsonify(data)


# methods=["POST"] wird angegeben wenn, daten vom client and die FlaskAPI "geposted" werden
@app.route("/add", methods=['POST'])
def add():
    data = request.json  # holt daten geposted vom client
    # TODO: Code zum hochladen/inserten der Daten aus der Datenbank


# client sendet Daten and die FlaskAPI und die FlaskAPI sendet dann andere oder dieselben Daten an den CLient
@app.route("/add", methods=['POST', 'GET'])
def add():
    data0 = request.json
    # TODO: Code der was mit den Daten macht und evtl. diese in die Datenbank schreibt
    # TODO: Code der Daten verarbeited oder von Datenbank holt
    data1 = []
    return jsonify(data1)


# Starten der FlaskAPI.
# Läuft parallel zu anderne Programmen/Scripts
if __name__ == '__main__':
    app.run(port=8888)  # Port an dem man mit der FlaskAPI kommunizieren kann.