-- Drop the database if it exists
DROP DATABASE IF EXISTS pizzeria;

-- Create a new database named pizzeria
CREATE DATABASE pizzeria;

-- Use the pizzeria database
USE pizzeria;

-- Create the 'pedido' table
CREATE TABLE pedido (
    nro_pedido INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(15),
    Direccion VARCHAR(30),
    Telefono INT,
    tipo VARCHAR(50),
    cantidad INT,
    precioFinal FLOAT
);

-- Create the 'producto' table with a foreign key reference to 'pedido'
CREATE TABLE producto (
    nroProducto INT AUTO_INCREMENT PRIMARY KEY,
    cantidad INT,
    precio FLOAT,
    tipoProducto VARCHAR(15),
    nro_pedido INT,
    FOREIGN KEY (nro_pedido) REFERENCES pedido(nro_pedido)
);

-- Create the 'tipoProducto' table with a foreign key reference to 'producto'
CREATE TABLE tipoProducto (
    nombre VARCHAR(20) PRIMARY KEY,
    nroProducto INT,
    FOREIGN KEY (nroProducto) REFERENCES producto(nroProducto)
);

-- Create the 'combos' table with a foreign key reference to 'producto'
CREATE TABLE combos (
    nombre VARCHAR(15) PRIMARY KEY,
    precio FLOAT,
    cantCombos INT,
    nroProducto INT,
    FOREIGN KEY (nroProducto) REFERENCES producto(nroProducto)
);

-- Define a trigger 'precio' for 'pedido' table
DELIMITER //
CREATE TRIGGER precio
BEFORE INSERT ON pedido
FOR EACH ROW
BEGIN
    IF NEW.tipo = 'Pizza' THEN
        SET NEW.precioFinal = 2500 * NEW.cantidad;
    ELSE
        SET NEW.precioFinal = 350 * NEW.cantidad;
    END IF;
END;
//
DELIMITER ;
