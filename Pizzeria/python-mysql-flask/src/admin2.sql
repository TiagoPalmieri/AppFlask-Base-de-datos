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
    precioFinal FLOAT,
    variedad varchar(25)
);

-- Define a trigger 'precio' for 'pedido' table
DELIMITER //
CREATE TRIGGER precio
BEFORE INSERT ON pedido
FOR EACH ROW
BEGIN
set @precioBebida  = CAST('0' AS DECIMAL(10, 2));

    if NEW.bebida = 'agua' then 
        set @precioBebida = 200;
    ELSE 
        set @precioBebida = 400;
    END IF;

    IF NEW.tipo = 'Pizza' THEN
        set NEW.precioFinal = 2500 * NEW.cantidad;
    ELSE
        set NEW.precioFinal = 350 * NEW.cantidad;
    END IF;

    set NEW.precioFinal = NEW.precioFinal + @precioBebida;

END;
//
DELIMITER ;
