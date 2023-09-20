
DROP TABLE HOTEL CASCADE CONSTRAINTS;
DROP TABLE CLIENTE CASCADE CONSTRAINTS;
DROP TABLE HABITACION CASCADE CONSTRAINTS;
DROP TABLE RESERVA CASCADE CONSTRAINTS;


--CREACION DE TABLAS

CREATE TABLE HOTEL(
id_hotel number(5) not null,
hotel_name varchar2(30) not null,
direccion varchar2(50) not null,
categoria varchar2(30) not null,
CONSTRAINT PK_HOTEL PRIMARY KEY(id_hotel));


CREATE TABLE CLIENTE(
id_cliente NUMBER(5) NOT NULL,
 nombre VARCHAR2(50) NOT NULL,  
 apellido VARCHAR2(50) NOT NULL, 
 correo VARCHAR2(20),
 fono_contacto NUMBER(10),
 CONSTRAINT PK_CLIENTE PRIMARY KEY(id_cliente));


CREATE TABLE HABITACION(
id_habitacion NUMBER(5)NOT NULL,
id_hotel NUMBER(5) not null,
tipo VARCHAR2(30) NOT NULL,
capacidad varchar2(30) NOT NULL,
precio VARCHAR2(50) NOT NULL,
descripcion VARCHAR2(500),
estado VARCHAR2(50) NOT NULL,
CONSTRAINT PK_HABITACION PRIMARY KEY(id_habitacion),
CONSTRAINT FK_HABITACION_HOTEL FOREIGN KEY(id_hotel) REFERENCES HOTEL(id_hotel));


CREATE TABLE RESERVA(
id_reserva NUMBER(9) NOT NULL,
id_cliente NUMBER(5) NOT NULL,
id_habitacion NUMBER(5) NOT NULL,
fecha_entrada DATE NOT NULL,
fecha_salida DATE NOT NULL,
cantidad_personas NUMBER(2) NOT NULL,
CONSTRAINT PK_RESERVA PRIMARY KEY(id_reserva),
CONSTRAINT FK_RESERVA_CLIENTE FOREIGN KEY(id_cliente) REFERENCES CLIENTE(id_cliente),
CONSTRAINT FK_HABITACION_HABITACION FOREIGN KEY(id_habitacion) REFERENCES HABITACION(id_habitacion));


INSERT INTO HOTEL(id_hotel,hotel_name,direccion,categoria) VALUES(001,'HOTEL PACIFIC REEF','Los leones #447','3 Estrellas');

INSERT INTO HABITACION(id_habitacion,id_hotel,tipo,capacidad,precio,descripcion,estado) 
    VALUES(001,001,'Estandar','1-2 Personas','$25.000 noche','Habitacion estandar','Disponible');
INSERT INTO HABITACION(id_habitacion,id_hotel,tipo,capacidad,precio,descripcion,estado) 
    VALUES(002,001,'Estandar','1-2 Personas','$25.000 noche','Habitacion estandar',' No Disponible');
INSERT INTO HABITACION(id_habitacion,id_hotel,tipo,capacidad,precio,descripcion,estado) 
    VALUES(003,001,'Estandar','1-2 Personas','$25.000 noche','Habitacion estandar','Disponible');
INSERT INTO HABITACION(id_habitacion,id_hotel,tipo,capacidad,precio,descripcion,estado) 
    VALUES(004,001,'Estandar','1-3 Personas','$35.000 noche','Habitacion con cama doble matrimonial + 1 individual y 1 baños','Disponible');
INSERT INTO HABITACION(id_habitacion,id_hotel,tipo,capacidad,precio,descripcion,estado) 
    VALUES(005,001,'Estandar','1-3 Personas','$35.000 noche','Habitacion con cama doble matrimonial + 1 individual y 1 baños','No Disponible');
INSERT INTO HABITACION(id_habitacion,id_hotel,tipo,capacidad,precio,descripcion,estado) 
    VALUES(006,001,'Estandar','1-3 Personas','$35.000 noche','Habitacion con cama doble matrimonial + 1 individual y 1 baños','Disponible');
INSERT INTO HABITACION(id_habitacion,id_hotel,tipo,capacidad,precio,descripcion,estado) 
    VALUES(007,001,'Estandar','1-4 Personas','$40.000 noche','Habitacion con 4 camas individuales y 2 baños ','No Disponible');
INSERT INTO HABITACION(id_habitacion,id_hotel,tipo,capacidad,precio,descripcion,estado) 
    VALUES(008,001,'Estandar','1-4 Personas','$40.000 noche','Habitacion con 4 camas individuales y 2 baños','Disponible');
INSERT INTO HABITACION(id_habitacion,id_hotel,tipo,capacidad,precio,descripcion,estado) 
    VALUES(009,001,'VIP','1-3 Personas','$50.000 noche','Camas premium + Vista cordillerana + servicio a habitacion','No Disponible');    
INSERT INTO HABITACION(id_habitacion,id_hotel,tipo,capacidad,precio,descripcion,estado) 
    VALUES(010,001,'VIP','1-3 Personas','$50.000 noche','Camas premium + Vista cordillerana + servicio a habitacion','Disponible');   
    

INSERT INTO CLIENTE(id_cliente, nombre, apellido, correo, fono_contacto) 
    VALUES(001,'Nicolas Alejandro','Lopez Mesa','NicoLopez@Gmail.com',123456789);

INSERT INTO RESERVA(id_reserva, id_cliente, id_habitacion, fecha_entrada, fecha_salida, cantidad_personas) 
    VALUES(001, 001, 002, '19/09/23', '23/09/23', 2);


    
SELECT * FROM CLIENTE;
SELECT * FROM habitacion;
SELECT * FROM RESERVA;
SELECT * FROM HOTEL;
