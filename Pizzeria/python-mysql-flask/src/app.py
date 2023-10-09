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

@app.route('/edit/<string:nro_pedido>', methods=['POST'])
def edit(nro_pedido):
    Nombre = request.form['Nombre']
    Direccion = request.form['Dirección']
    Telefono = request.form['Telefono']
    tipo = request.form['tipo']
    cantidad = int(request.form['cantidad'])  # Convert cantidad to an integer

    if Nombre and Direccion and Telefono and tipo and cantidad:
        cursor = db.database.cursor()

        # Define multiplication factors based on tipo
        if tipo == "Pizza":
            multiplicador = 2500
        elif tipo == "Empanadas":
            multiplicador = 350
        else:
            multiplicador = 0  # Default to 0 if tipo is not recognized

        # Calculate the new precioFinal as an integer
        nuevo_precioFinal = multiplicador * cantidad

        # Update the pedido record with the new values
        sql = "UPDATE pedido SET Nombre = %s, Direccion = %s, Telefono = %s, tipo = %s, cantidad = %s, precioFinal = %s WHERE nro_pedido = %s"
        data = (Nombre, Direccion, Telefono, tipo, cantidad, nuevo_precioFinal, nro_pedido)
        cursor.execute(sql, data)
        db.database.commit()

    return redirect(url_for('home'))

@app.route('/delete/<string:nro_pedido>')
def delete(nro_pedido):
    cursor = db.database.cursor()
    sql = "DELETE FROM pedido WHERE nro_pedido=%s"
    data = (nro_pedido,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)