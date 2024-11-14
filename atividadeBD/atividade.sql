CREATE DATABASE usuarios;

create table veiculos(
    id_veiculos integer primary Key AUTO_INCREMENT,
    marca varchar(50) not Null,
    modelo varchar(50) not Null, 
    placa varchar(50) not Null,
    ano int(8) not null,
    valor_diaria decimal(10)
    );