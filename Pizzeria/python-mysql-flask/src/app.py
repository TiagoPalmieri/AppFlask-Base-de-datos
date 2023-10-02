from flask import Flask, render_template, request, redirect, url_for
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
    Nombre = request.form['Nombre']
    Direccion = request.form['Dirección']
    Telefono = request.form['Telefono']
    tipo = request.form['tipo']
    cantidad = request.form['cantidad']

    if Nombre and Direccion and Telefono and tipo and cantidad:
        cursor = db.database.cursor()
        sql = "INSERT INTO pedido (Nombre, Direccion, Telefono, tipo, cantidad) VALUES (%s, %s, %s, %s, %s)"
        data = (Nombre, Direccion, Telefono, tipo, cantidad)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', method=['POST'])
def edit(id):
    Nombre = request.form['Nombre']
    Direccion = request.form['Dirección']
    Telefono = request.form['Telefono']
    tipo = request.form['tipo']
    cantidad = request.form['cantidad']

    if Nombre and Direccion and Telefono and tipo and cantidad:
        cursor = db.database.cursor()
        sql = "UPDATE pedido SET Nombre = %s, Direccion = %s, Telefono = %s, tipo = %s, cantidad = %s WHERE id = %s"
        data = (Nombre, Direccion, Telefono, tipo, cantidad, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM pedido WHERE id=%s)"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)