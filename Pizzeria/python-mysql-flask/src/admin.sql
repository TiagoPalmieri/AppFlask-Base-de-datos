drop database if exists pizzeria;

create database pizzeria;

use pizzeria;

create table
    pedido (
        nro_pedido int auto_increment primary key,
        Nombre varchar(15),
        Direccion varchar(30),
        Telefono int,
        tipo VARCHAR(50),
        cantidad int,
        precioFinal float
    );

create table
    producto (
        nroProducto int auto_increment primary key,
        cantidad int,
        precio float,
        tipoProducto varchar(15),
        nro_pedido int,
        foreign key(nro_pedido) references pedido(nro_pedido)
    );

create table
    tipoProducto (
        nombre varchar(20) primary key,
        nroProducto int,
        foreign key(nroProducto) references producto(nroProducto)
    );

create table
    combos (
        nombre varchar(15) primary key,
        precio float,
        cantCombos int,
        nroProducto int,
        foreign key(nroProducto) references producto(nroProducto)
    );

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