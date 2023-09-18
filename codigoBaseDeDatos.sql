drop database if exists pizzeria;
create database pizzeria;
use pizzeria;

create table pedido (
nro_pedido int auto_increment primary key,
cantidad int,
precioFinal float,
nroTelefono int,
direccion varchar (30),
nombreCliente varchar(15)
);

create table producto (
nroProducto int auto_increment primary key,
cantidad int,
precio float,
tipoProducto varchar(15),
nro_pedido int,
foreign key(nro_pedido) references pedido(nro_pedido)
);

create table tipoProducto (
nombre varchar(20) primary key,
nroProducto int,
foreign key(nroProducto) references producto(nroProducto)
);

create table combos (
nombre varchar(15) primary key,
precio float,
cantCombos int,
nroProducto int,
foreign key(nroProducto) references producto(nroProducto)
);
