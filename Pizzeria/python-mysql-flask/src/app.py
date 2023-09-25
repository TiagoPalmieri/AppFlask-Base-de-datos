from flask import Flask, render_template, request 
import os
import database as db

#pip install flask
#pip install mysql-connector-python

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)


#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM pedido")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

#Ruta para guardar pedidos en la db
@app.route('/user', methods=['POST'])
def addPedido():
    nombre = request.form['Nombre']
    direccion = request.form['Dirección']
    telefono = request.form['Telefono']

    if nombre and direccion and telefono:
        cursor = db.database.cursor()
        sql = "INSERT INTO pedido (nombre, direccion, telefono) VALUES"



if __name__ == '__main__':
    app.run(debug=True, port=4000)