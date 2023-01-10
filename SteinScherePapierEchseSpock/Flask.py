from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'swp_rubner'
app.config['MYSQL_PASSWORD'] = 'swp_rubner202223'
app.config['MYSQL_DB'] = 'swp_rubner_stpes'

mysql = MySQL(app)


# Funktionsname kann anders heißen
@app.route("/")
def start():
    return "start message"


# Routen- und Funktionsname kann anders heißen
# methods=["GET"] muss angegeben werden, wenn man als client Daten von der FlaskAPI haben will
"""@app.route("/get", methods=['GET'])
def get():
    # TODO: Code zum Holen der Daten aus Datenbank (sqlLite, mySQL, ...)
    sql = "select * from table"
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    # TODO: select statement and result handling missing
    data = []
    return jsonify(data)
"""

# client sendet Daten and die FlaskAPI und die FlaskAPI sendet dann andere oder dieselben Daten an den CLient
@app.route("/add", methods=['POST', 'GET'])
def add():
    data0 = request.json
    data0 = [data0[key] for key in data0]
    print(data0)
    cursor = mysql.connection.cursor()
    cursor.execute(
        "insert into FLASK_STUFF(player_hand, pick_count) values (%s, %s) on duplicate key update pick_count = %s;",
        data0 + [data0[-1]]
    )
    mysql.connection.commit()

    # TODO: Code der was mit den Daten macht und evtl. diese in die Datenbank schreibt
    # TODO: Code der Daten verarbeited oder von Datenbank holt
    data1 = ["uploaded"]
    return jsonify(data1)


# Starten der FlaskAPI.
# Läuft parallel zu anderne Programmen/Scripts
if __name__ == '__main__':
    app.run(port=8888)  # Port an dem man mit der FlaskAPI kommunizieren kann.
