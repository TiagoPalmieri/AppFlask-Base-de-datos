-- Drop the database if it exists
DROP DATABASE IF EXISTS pizzeria;

-- Create a new database named pizzeria
CREATE DATABASE pizzeria;

-- Use the pizzeria database
USE pizzeria;

-- Create the 'pedido' table
CREATE TABLE pedido (
    nro_pedido INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(30),
    Direccion VARCHAR(30),
    Telefono INT,
    tipo VARCHAR(50),
    cantidad INT,
    bebida VARCHAR(50),
    entrega VARCHAR(50),
    precioFinal FLOAT
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
