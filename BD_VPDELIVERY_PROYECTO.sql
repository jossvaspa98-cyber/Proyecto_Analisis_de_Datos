
----------------------------------------------Creacion de la base de datos----------------------------------------------------------- 
CREATE  DATABASE BD_VPDELIVERY
GO


--------------------------------Indicacion de la base de datos con la que se va a trabajar----------------------------------------------------------- 
USE BD_VPDELIVERY
GO --Fin del lote de trabajo



-----------------------------------------------------Tabla Clientes----------------------------------------------------------------------------------
                                 -------------------------DDL--------------------------

CREATE TABLE CLIENTES (

	--Se construye la tabla con todos los datos requeridos 
	--Se asigna la que será la llave primaria con auto incremento 
	id_cliente BIGINT IDENTITY (1,1),
	nom_cliente VARCHAR (20) NOT NULL,
	apellido1 VARCHAR (20) NOT NULL,
	apellido2 VARCHAR (20) NULL,
	correo_electronico VARCHAR (50) NOT NULL,
	ced_cliente int NOT NULL,
	direccion_cliente VARCHAR (60) NOT NULL,
	id_distrito BIGINT NOT NULL

	--Se realiza la restriccion de llave primaria
	CONSTRAINT PK_id_cliente PRIMARY KEY (id_cliente)

);
GO --Fin del lote de trabajo

----------------------------------------------------------Tabla Agentes----------------------------------------------------------------------------------
                                 ------------------------------DDL-----------------------------------
CREATE TABLE AGENTES (

	--Se construye la tabla con todos los datos requeridos 
	--Se asigna la que será la llave primaria con auto incremento 
	id_agente BIGINT IDENTITY (1,1),
	nom_agente VARCHAR (15) NOT NULL,
	apellido1 VARCHAR (20) NOT NULL,
	apellido2 VARCHAR (20) NULL,
	correo_agente VARCHAR (50) NOT NULL,
	ced_agente INT NOT NULL,
	id_distrito BIGINT NOT NULL,
	fecha_nacimiento date NOT NULL

	--Se realiza la restriccion de llave primaria
	CONSTRAINT PK_id_agente PRIMARY KEY (id_agente)

);
GO --Fin del lote de trabajo
-------------------------------------------------------Tabla Negocios Afiliados----------------------------------------------------------------------------------
                                       --------------------------DDL----------------------------
CREATE TABLE NEGOCIOS_AFILIADOS (

	--Se construye la tabla con todos los datos requeridos 
	--Se asigna la que será la llave primaria con auto incremento 
	id_negocio BIGINT IDENTITY (1,1),
	nom_negocio VARCHAR (20) NOT NULL,
	ced_juridica VARCHAR (20) NOT NULL,
	direccion VARCHAR (50) NOT NULL,
	id_distrito BIGINT NOT NULL

	--Se realiza la restriccion de llave primaria
	CONSTRAINT PK_id_negocio PRIMARY KEY (id_negocio)

);
GO --Fin del lote de trabajo
-------------------------------------------------------Tabla Provincias----------------------------------------------------------------------------------
                                   -------------------------DDL---------------------------
CREATE TABLE PROVINCIAS (

	--Se construye la tabla con todos los datos requeridos 
	--Se asigna la que será la llave primaria con auto incremento 
	id_provincia INT IDENTITY (1,1),
	nom_provincia VARCHAR (20),

	--Se realiza la restriccion de llave primaria
	CONSTRAINT PK_id_provincia PRIMARY KEY (id_provincia)


);
GO --Fin del lote de trabajo
-------------------------------------------------------Tabla Cantones----------------------------------------------------------------------------------
                                  --------------------------DDL----------------------------
CREATE TABLE CANTONES (

	--Se construye la tabla con todos los datos requeridos 
	--Se asigna la que será la llave primaria con auto incremento 
	id_canton BIGINT IDENTITY (1,1),
	nom_canton VARCHAR (20) NOT NULL,
	id_provincia INT NOT NULL

	--Se realiza la restriccion de llave primaria
	CONSTRAINT PK_id_canton PRIMARY KEY (id_canton)
);
GO --Fin del lote de trabajo
------------------------------------------------------Tabla Distritos----------------------------------------------------------------------------------
                                  --------------------------DDL------------------------------
CREATE TABLE DISTRITOS (

	--Se construye la tabla con todos los datos requeridos 
	--Se asigna la que será la llave primaria con auto incremento 
	id_distrito BIGINT IDENTITY (1,1),
	nom_distrito VARCHAR (20) NOT NULL,
	id_canton BIGINT NOT NULL
	--Se realiza la restriccion de llave primaria
	CONSTRAINT PK_id_distrito PRIMARY KEY (id_distrito)

);
GO --Fin del lote de trabajo
--------------------------------------------------------Tabla Entregas----------------------------------------------------------------------------------
                                  ---------------------------DDL-------------------------------
CREATE TABLE ENTREGAS ( 
	
	--Se construye la tabla con todos los datos requeridos 
	--Se asigna la que será la llave primaria con auto incremento 
	id_entrega BIGINT IDENTITY (1,1),
	id_agente BIGINT NOT NULL,
	id_tipo_vehiculo SMALLINT NOT NULL,
	id_cliente BIGINT NOT NULL,
	id_negocio BIGINT NOT NULL,
	fecha DATE NOT NULL,
	hora_entrada_entrega TIME NOT NULL,
	estado_entrega VARCHAR (12) NOT NULL,
	hora_entregado TIME NULL,
	distancia_entrega DECIMAL (5,2) NOT NULL,
	peso_paquete DECIMAL (5,2) NOT NULL,
	impuesto DECIMAL (5,2) NOT NULL,
	bono DECIMAL (5,2) NULL,
	total_pago MONEY NOT NULL
	
	--Se realiza la restriccion de llave primaria
	CONSTRAINT PK_id_entrega PRIMARY KEY (id_entrega)

);
GO --Fin del lote de trabajo
-------------------------------------------------------Tabla Salarios Agentes----------------------------------------------------------------------------------
                                     ---------------------------DDL-------------------------------
CREATE TABLE SALARIOS_AGENTES (

	--Se construye la tabla con todos los datos requeridos 
	--Se asigna la que será la llave primaria con auto incremento 
	id_salario BIGINT IDENTITY (1,1),
	id_agente BIGINT NOT NULL,
	fecha_salarios DATE NOT NULL,
	salario_bruto MONEY NOT NULL,
	carga_social DECIMAL (5,2) NOT NULL,
	rebajo_vehiculo DECIMAL (5,2) NULL,
	rebajo_aplicacion DECIMAL (5,2) NOT NULL,
	salario_neto MONEY NOT NULL

	--Se realiza la restriccion de llave primaria
	CONSTRAINT PK_id_salario PRIMARY KEY (id_salario)

);
GO --Fin del lote de trabajo
-------------------------------------------------------Tabla Tipos de Vehiculos----------------------------------------------------------------------------------
                                        -------------------------DDL--------------------------
CREATE TABLE TIPOS_VEHICULOS (

	--Se construye la tabla con todos los datos requeridos 
	--Se asigna la que será la llave primaria con auto incremento
	id_tipo SMALLINT IDENTITY  (1,1),
	tipo_vehiculo VARCHAR (10)

	--Se realiza la restriccion de llave primaria
	CONSTRAINT PK_id_tipo PRIMARY KEY (id_tipo)

);
GO --Fin del lote de trabajo
------------------------------------------------------------Tabla de Vehiculos----------------------------------------------------------------------------------
                                    --------------------------------DDL-----------------------------------
CREATE TABLE VEHICULOS (

	--Se construye la tabla con todos los datos requeridos 
	--Se asigna la que será la llave primaria con auto incremento
	
	--Llave foranea
	id_agente BIGINT NOT NULL, 
	placa VARCHAR (8) NULL,
	marca VARCHAR (20) NOT NULL,
	modelo VARCHAR (20) NOT NULL,
	--Llave foranea
	id_tipo SMALLINT NOT NULL

);
GO --Fin del lote de trabajo

------------------------------------------------------------Tabla de Telefonos----------------------------------------------------------------------------------
                                    --------------------------------DDL-----------------------------------
CREATE TABLE TELEFONOS (

	--Se construye la tabla con todos los datos requeridos 
	--Se asigna la que será la llave primaria con auto incremento
	id_telefono BIGINT IDENTITY (1,1),
	num_telefono VARCHAR (20),
	tipo_telefono VARCHAR (8)

	--Se realiza la restriccion de llave primaria
	CONSTRAINT PK_id_telefono PRIMARY KEY (id_telefono)

);
GO --Fin del lote de trabajo
----------------------------------------------------Tabla detalle Telefonos Clientes----------------------------------------------------------------------------------
                                           -------------------------DDL--------------------------
CREATE TABLE TELEFONOS_CLIENTES (
	
	--Llave foranea
	id_cliente BIGINT,
	--Llave foranea
	id_telefono BIGINT 

	--Se realiza la restriccion de llaves primarias
	CONSTRAINT PK_talefono_cliente PRIMARY KEY (id_cliente, id_telefono)
	
);
GO --Fin del lote de trabajo
-------------------------------------------------------Tabla Detalle Telefonos Agentes----------------------------------------------------------------------------------
                                            ------------------------DDL----------------------------
CREATE TABLE TELEFONOS_AGENTES (
	
	--Llave foranea
	id_agente BIGINT, 
	--Llave foranea
	id_telefono BIGINT 

	--Se realiza la restriccion de llaves primarias
	CONSTRAINT PK_talefono_agente PRIMARY KEY (id_agente, id_telefono)
);
GO --Fin del lote de trabajo
------------------------------------------------------Tabla detalle Telefonos Negocio----------------------------------------------------------------------------------
                                           ------------------------DDL-------------------------
CREATE TABLE TELEFONOS_NEGOCIOS (

	--Llave foranea
	id_negocio BIGINT,
	--Llave foranea
	id_telefono BIGINT 

	--Se realiza la restriccion de llaves primarias
	CONSTRAINT PK_talefono_negocio PRIMARY KEY (id_negocio, id_telefono)

);
GO--Fin del lote de trabajo

-------------------------------------------------------Restricciones Tabla Clientes----------------------------------------------------------------------------------
                                          --------------------------DDL-------------------------

ALTER TABLE CLIENTES
ADD
	--Creacion de la restriccion del id_distrito como llave foranea
	--que hace referencia a la tabla de DISTRITOS
	CONSTRAINT FK_id_distrito FOREIGN KEY (id_distrito ) 
	REFERENCES DISTRITOS (id_distrito),

	--Se indica la restriccion del correo electronico y cedula como datos unicos
	CONSTRAINT UN_correo_cliente UNIQUE (correo_electronico),
	CONSTRAINT UN_ced_cliente UNIQUE (ced_cliente)
;
GO --Fin del lote de trabajo

--------------------------------------------------------Restricciones Tabla Agentes----------------------------------------------------------------------------------
                                         ---------------------------DDL-------------------------------
ALTER TABLE AGENTES
ADD
	
	--Creacion de la restriccion del id_distrito como llave foranea
	--que hace referencia a la tabla de DISTRITOS
	CONSTRAINT FK_id_distrito_agente FOREIGN KEY (id_distrito) 
	REFERENCES DISTRITOS (id_distrito),

	--Se indica la restriccion del correo electronico y cedula como datos unicos
	CONSTRAINT UN_correo_agente UNIQUE (correo_agente),
	CONSTRAINT UN_ced_agente UNIQUE (ced_agente)
;
GO --Fin del lote de trabajo

-------------------------------------------------------Restricciones Tabla Negocios----------------------------------------------------------------------------------
                                          --------------------------DDL-----------------------------------
ALTER TABLE NEGOCIOS_AFILIADOS
ADD
	--Creacion de la restriccion del id_distrito como llave foranea
	--que hace referencia a la tabla de DISTRITOS
	CONSTRAINT FK_id_distrito_negocio FOREIGN KEY (id_distrito) 
	REFERENCES DISTRITOS (id_distrito)
;
GO --Fin del lote de trabajo

-------------------------------------------------------Restricciones Tabla Cantones----------------------------------------------------------------------------------
                                          --------------------------DDL----------------------
ALTER TABLE CANTONES
ADD
	--Creacion de la restriccion del id_provincia como llave foranea
	--que hace referencia a la tabla de PROVINCIAS
	CONSTRAINT FK_id_provincia_canton FOREIGN KEY (id_provincia) 
	REFERENCES PROVINCIAS (id_provincia) 
;
GO --Fin del lote de trabajo

--------------------------------------------------------Restricciones Tabla Distritos----------------------------------------------------------------------------------
											-------------------------DDL------------------------

ALTER TABLE DISTRITOS
ADD
	--Creacion de la restriccion del id_cantones como llave foranea
	--que hace referencia a la tabla de CANTONES
	CONSTRAINT FK_id_canton_distrito FOREIGN KEY (id_canton) 
	REFERENCES CANTONES (id_canton) 
;
GO --Fin del lote de trabajo

---------------------------------------------------------Restricciones Tabla Entregas----------------------------------------------------------------------------------
										-----------------------------DDL-------------------------

ALTER TABLE ENTREGAS
ADD
	--Creacion de la restriccion del id_agente como llave foranea
	--que hace referencia a la tabla de AGENTES
	CONSTRAINT FK_id_agente FOREIGN KEY (id_agente) 
	REFERENCES AGENTES (id_agente), 

	--Creacion de la restriccion del id_cliente como llave foranea
	--que hace referencia a la tabla de CLIENTES
	CONSTRAINT FK_id_cliente FOREIGN KEY (id_cliente) 
	REFERENCES CLIENTES (id_cliente),

	--Creacion de la restriccion del id_negocio como llave foranea
	--que hace referencia a la tabla de los NEGOCIOS_AFILIADOS
	CONSTRAINT FK_id_negocio FOREIGN KEY (id_negocio) 
	REFERENCES NEGOCIOS_AFILIADOS (id_negocio),

	--Creacion de la restriccion del id_vehiculos como llave foranea
	--que hace referencia a la tabla de TIPOS_VEHICULOS
	CONSTRAINT FK_id_tipo_vehiculo FOREIGN KEY (id_tipo_vehiculo) 
	REFERENCES TIPOS_VEHICULOS (id_tipo),

	--Se indica la restriccion del estado de la entrega unicamente 
	--con el estado Entregado o Pendiente
	CONSTRAINT CK_estado_entrega 
	CHECK (estado_entrega = 'Entregado' OR estado_entrega = 'Pendiente'),

	--Se indica que el estado Pendiente estará indicado por defecto
	CONSTRAINT DF_estado_entrega DEFAULT 'Pendiente' FOR estado_entrega,
	
	--Se indica que el peso de los paquetes tendra que ser menor o igual a 100kg
	CONSTRAINT CK_peso_paquete 
	CHECK (peso_paquete <= 100),

	--Se asignará una fecha por defecto
	CONSTRAINT DF_fecha DEFAULT getdate() FOR fecha


GO --Fin del lote de trabajo

----------------------------------------------------------Restricciones Tabla Salarios----------------------------------------------------------------------------------
										------------------------------DDL---------------------------

ALTER TABLE SALARIOS_AGENTES
ADD

	--Creacion de la restriccion del id_agente como llave foranea
	--que hace referencia a la tabla de AGENTES
	CONSTRAINT FK_id_agente2 FOREIGN KEY (id_agente) 
	REFERENCES AGENTES (id_agente),

	--Se asignará una fecha por defecto
	CONSTRAINT DF_fecha_salario DEFAULT getdate() FOR fecha_salarios
;
GO --Fin del lote de trabajo

-----------------------------------------------------Restricciones Tabla Vehiculos----------------------------------------------------------------------------------
											---------------------DDL------------------------------

ALTER TABLE VEHICULOS
ADD
	--Creacion de la restriccion del id_agente como llave foranea
	--que hace referencia a la tabla de AGENTES

	CONSTRAINT FK_id_agente3 FOREIGN KEY (id_agente) 
	REFERENCES AGENTES (id_agente),
	
	--Creacion de la restriccion del id_tipo como llave foranea
	--que hace referencia a la tabla de TIPOS_VEHICULOS 
	CONSTRAINT FK_id_tipo FOREIGN KEY (id_tipo) 
	REFERENCES TIPOS_VEHICULOS (id_tipo) 

;
GO --Fin del lote de trabajo

--Se agregó la tupla de id_vehiculo como PRIMARY KEY  
ALTER TABLE VEHICULOS 
ADD id_vehiculo BIGINT IDENTITY (1,1)
	CONSTRAINT PK_id_vehiculo PRIMARY KEY (id_vehiculo)
GO

-------------------------------------------------Restricciones Tabla Tipos de Vehiculos----------------------------------------------------------------------------------
												----------------------DDL---------------------

ALTER TABLE TIPOS_VEHICULOS
ADD
	
	--Se indica la restriccion del tipo de vehiculo de la tabla TIPOS_VEHICULOS
	--unicamente con los tipos carro, moto, bicicleta
	CONSTRAINT CK_tipo_vehiculo 
	CHECK ((tipo_vehiculo = 'Carro') OR (tipo_vehiculo = 'Moto') OR (tipo_vehiculo = 'Bicicleta')),

	--Se indica que el tipo de vehiculo 'moto' estará indicada por defecto
	CONSTRAINT DF_tipo_vehiculo DEFAULT 'Moto' FOR tipo_vehiculo
;
GO --Fin del lote de trabajo

------------------------------------------------------Restricciones Tabla Telefonos----------------------------------------------------------------------------------
											-----------------------DDL-----------------------

ALTER TABLE TELEFONOS
ADD
	
	--Se indica la restriccion del tipo de telefono de la tabla TELEFONOS
	--unicamente con los tipos 'casa', 'celular', 'oficina'
	CONSTRAINT CK_tipo_telefono
	CHECK ((tipo_telefono = 'Casa') OR (tipo_telefono = 'Celular') OR (tipo_telefono = 'Oficina')),

	--Se indica que el tipo de telefono 'celular' estará indicada por defecto
	CONSTRAINT DF_tipo_telefono DEFAULT 'Celular' FOR tipo_telefono

;
GO --Fin del lote de trabajo

---------------------------------------------------Restricciones Tabla Telefonos Clientes----------------------------------------------------------------------------------
												--------------------DDL------------------------

ALTER TABLE TELEFONOS_CLIENTES
ADD
	--Creacion de la restriccion del id_cliente como llave foranea
	--que hace referencia a la tabla de TELEFONOS_CLIENTES
	CONSTRAINT FK_telefono_cliente FOREIGN KEY (id_cliente) 
	REFERENCES CLIENTES (id_cliente),

	--Creacion de la restriccion del id_telefono como llave foranea
	--que hace referencia a la tabla de TELEFONOS
	CONSTRAINT FK_telefono_cliente1  FOREIGN KEY (id_telefono) 
	REFERENCES TELEFONOS (id_telefono) 

;
GO --Fin del lote de trabajo

-----------------------------------------------------Restricciones Tabla Telefonos Agentes----------------------------------------------------------------------------------
												--------------------DDL------------------

ALTER TABLE TELEFONOS_AGENTES
ADD
	--Creacion de la restriccion del id_agente como llave foranea
	--que hace referencia a la tabla de TELEFONOS_CLIENTES
	CONSTRAINT FK_telefono_agente FOREIGN KEY (id_agente) 
	REFERENCES AGENTES (id_agente),

	--Creacion de la restriccion del id_telefono como llave foranea
	--que hace referencia a la tabla de TELEFONOS
	CONSTRAINT FK_telefono_agente1  FOREIGN KEY (id_telefono) 
	REFERENCES TELEFONOS (id_telefono)

;
GO --Fin del lote de trabajo

----------------------------------------------------Restricciones Tabla Negocios----------------------------------------------------------------------------------
											---------------------DDL--------------------

ALTER TABLE TELEFONOS_NEGOCIOS
ADD
	--Creacion de la restriccion del id_negocios como llave foranea
	--que hace referencia a la tabla de TELEFONOS_CLIENTES
	CONSTRAINT FK_telefono_negocio FOREIGN KEY (id_negocio) 
	REFERENCES  NEGOCIOS_AFILIADOS (id_negocio),

	--Creacion de la restriccion del id_telefono como llave foranea
	--que hace referencia a la tabla de TELEFONOS
	CONSTRAINT FK_telefono_cliente2  FOREIGN KEY (id_telefono) 
	REFERENCES TELEFONOS (id_telefono)

;
GO --Fin del lote de trabajo

-----------------------------------------------Datos tabla Provincias----------------------------------------------------------------------------------
									------------------DML-----------------

--Se insertan los datos de todos las provincias
INSERT INTO PROVINCIAS(nom_provincia)
VALUES('Alajuela')
GO
INSERT INTO PROVINCIAS(nom_provincia)
VALUES('San Jose')
GO
INSERT INTO PROVINCIAS(nom_provincia)
VALUES('Heredia')
GO
INSERT INTO PROVINCIAS(nom_provincia)
VALUES('Cartago')
GO
INSERT INTO PROVINCIAS(nom_provincia)
VALUES('Limon')
GO
INSERT INTO PROVINCIAS(nom_provincia)
VALUES('Guanacaste')
GO
INSERT INTO PROVINCIAS(nom_provincia)
VALUES('Puntarenas')
GO

-----------------------------------------------Datos tabla Cantones----------------------------------------------------------------------------------
									------------------DML---------------------

--Se insertan los datos de todos los cantones
--ALAJUELA
INSERT INTO CANTONES(nom_canton,id_provincia)
VALUES('San Ramon',1)
GO
INSERT INTO CANTONES(nom_canton,id_provincia)
VALUES('Palmares',1)
GO

---------------------------------------------------------
--SAN JOSE
INSERT INTO CANTONES(nom_canton,id_provincia)
VALUES('Escazu',2)
GO
INSERT INTO CANTONES(nom_canton,id_provincia)
VALUES('San Jose',2)
GO
---------------------------------------------------------
--HEREDIA
INSERT INTO CANTONES(nom_canton,id_provincia)
VALUES('Heredia',3)
GO
INSERT INTO CANTONES(nom_canton,id_provincia)
VALUES('Barva',3)
GO

-------------------------------------------------Datos tabla Distritos----------------------------------------------------------------------------------
								------------------------DML-----------------------

--SAN RAMON
--ID 1
INSERT INTO DISTRITOS(nom_distrito,id_canton) 
VALUES('San Ramon',1)
GO
--ID 2
INSERT INTO DISTRITOS(nom_distrito,id_canton) 
VALUES('San Juan',1)
GO
---------------------------------------------------------
--PALMARES
--ID 3
INSERT INTO DISTRITOS(nom_distrito,id_canton) 
VALUES('Palmares',2)
GO
--ID 4
INSERT INTO DISTRITOS(nom_distrito,id_canton) 
VALUES('Zaragoza',2)
GO
---------------------------------------------------------
--ESCAZU
--ID 5
INSERT INTO DISTRITOS(nom_distrito,id_canton) 
VALUES('Escazu',3)
GO
---------------------------------------------------------
--SAN JOSE
--ID 6
INSERT INTO DISTRITOS(nom_distrito,id_canton) 
VALUES('La Uruca',4)
GO
--ID 7
INSERT INTO DISTRITOS(nom_distrito,id_canton) 
VALUES('Zapote',4)
GO
---------------------------------------------------------
--HEREDIA
--ID 8
INSERT INTO DISTRITOS(nom_distrito,id_canton) 
VALUES('Heredia',5)
GO
--ID 9
INSERT INTO DISTRITOS(nom_distrito,id_canton) 
VALUES('Mercedes',5)
GO

------------------------------------------------Datos de los Clientes----------------------------------------------------------------------------------
									--------------------DML-----------------------

--Se insertan los datos de todos los clientes
--ID 1
INSERT INTO CLIENTES(nom_cliente,apellido1,apellido2, correo_electronico,ced_cliente,direccion_cliente,id_distrito)
VALUES('Carlos','Rojas','Jimenez','carjim_12@gmail.com',208660215,'800mts norte del templo catolico, Palmares',3)
GO
--ID 2
INSERT INTO CLIENTES(nom_cliente,apellido1,apellido2, correo_electronico,ced_cliente,direccion_cliente,id_distrito)
VALUES('Miguel','Rodriguez',NULL,'miguerod_15@gmail.com',207580314,'Al costado oeste de almacenes el rey, San Ramon',1)
GO
--ID 3
INSERT INTO CLIENTES(nom_cliente,apellido1,apellido2, correo_electronico,ced_cliente,direccion_cliente,id_distrito)
VALUES('Andrea','Pacheco','Hernandez','andrepach_02@gmail.com',106870925,'200mts norte del antiguo edificio de transito, San Ramon',2)
GO
--ID 4
INSERT INTO CLIENTES(nom_cliente,apellido1,apellido2, correo_electronico,ced_cliente,direccion_cliente,id_distrito)
VALUES('Catalina','Fernandez','Oviedo','catafer_20@gmail.com',207900531,'350mts suroeste de la impenta Acosta, Palmares',4)
GO
--ID 5
INSERT INTO CLIENTES(nom_cliente,apellido1,apellido2, correo_electronico,ced_cliente,direccion_cliente,id_distrito)
VALUES('Diego','Paniagua','Guillen','diepan_19@gmail.com',207654321,'Contiguo a las oficinas de la CCSS, San  Ramón',1)
GO
--ID 6
INSERT INTO CLIENTES(nom_cliente,apellido1,apellido2, correo_electronico,ced_cliente,direccion_cliente,id_distrito)
VALUES('Sofia','Arias','Sanchez','sofisanch_05@gmail.com',206870925,'Costado sur de la iglesia catolica, Alajuela, Palmares',3)
GO
--ID 7
INSERT INTO CLIENTES(nom_cliente,apellido1,apellido2, correo_electronico,ced_cliente,direccion_cliente,id_distrito)
VALUES('Ricardo','Artavia',NULL,'richiart_10@gmail.com',209135705,'Esquina oeste del bar de Quillo,Palmares',3)
GO
--ID 8
INSERT INTO CLIENTES(nom_cliente,apellido1,apellido2, correo_electronico,ced_cliente,direccion_cliente,id_distrito)
VALUES('Pablo','Vasquez','Mora','pablovas_56@gmail.com',206870932,'25mts oeste de la esquina suroeste del parque, San Ramon',1)
GO
--ID 9
INSERT INTO CLIENTES(nom_cliente,apellido1,apellido2, correo_electronico,ced_cliente,direccion_cliente,id_distrito)
VALUES('Maria','Salas','Cespedes','marices_78@gmail.com',203456789,'25 mts oeste de correos de Costa Rica, Palmares',3)
GO
--ID 10
INSERT INTO CLIENTES(nom_cliente,apellido1,apellido2, correo_electronico,ced_cliente,direccion_cliente,id_distrito)
VALUES('Karla','Loria','Suarez','Karlori_16@gmail.com',209210675,'Contiguo a Bugys Patriarca, San Ramon',1)
GO

---------------------------------------------------Datos de los Agentes----------------------------------------------------------------------------------
								--------------------------DML---------------------

--Se insertan los datos de todos los agentes
--ID 1
INSERT INTO AGENTES(nom_agente,apellido1,apellido2,correo_agente,ced_agente,fecha_nacimiento,id_distrito)
VALUES('Guillermo','Sanchez','Hidalgo','guilleSanchez_42@gmail.com',407530170,'19830513',1)
GO
--ID 2
INSERT INTO AGENTES(nom_agente,apellido1,apellido2,correo_agente,ced_agente,fecha_nacimiento,id_distrito)
VALUES('Orlando','Gomez','Najera','orligomez_70@gmail.com',202156911,'19960220',1)
GO
--ID 3
INSERT INTO AGENTES(nom_agente,apellido1,apellido2,correo_agente,ced_agente,fecha_nacimiento,id_distrito)
VALUES('Marta','Gonsalez','Solano','margon_72@gmail.com',204951881,'19950421',3)
GO
--ID 4
INSERT INTO AGENTES(nom_agente,apellido1,apellido2,correo_agente,ced_agente,fecha_nacimiento,id_distrito)
VALUES('Laura','Castro','Rivas','laucas_87@gmail.com',102050910,'19910607',1)
GO
--ID 5
INSERT INTO AGENTES(nom_agente,apellido1,apellido2,correo_agente,ced_agente,fecha_nacimiento,id_distrito)
VALUES('Enrique','Lizano','Rojas','EnriLiz_50@gmail.com',203425302,'19951126',3)
GO
--ID 6
INSERT INTO AGENTES(nom_agente,apellido1,apellido2,correo_agente,ced_agente,fecha_nacimiento,id_distrito)
VALUES('Marcela','Quiros','Jimenez','marcequiros_46@gmail.com',201035783,'19890715',1)
GO
--ID 7
INSERT INTO AGENTES(nom_agente,apellido1,apellido2,correo_agente,ced_agente,fecha_nacimiento,id_distrito)
VALUES('Maria','Araya','Mendez','mariaAray_90@gmail.com',202156963,'19920419',3)
GO
--ID 8
INSERT INTO AGENTES(nom_agente,apellido1,apellido2,correo_agente,ced_agente,fecha_nacimiento,id_distrito)
VALUES('Lorenzo','Morera','Fernandez','lorenzmore_53@gmail.com',209938722,'19911222',3)
GO
--ID 9
INSERT INTO AGENTES(nom_agente,apellido1,apellido2,correo_agente,ced_agente,fecha_nacimiento,id_distrito)
VALUES('Rebeca','Fonseca','Masis','rebefonse_30@gmail.com',203279923,'19961104',1)
GO
--ID 10
INSERT INTO AGENTES(nom_agente,apellido1,apellido2,correo_agente,ced_agente,fecha_nacimiento,id_distrito)
VALUES('Marcos','Solis','Jimenez','marcsoli_21@gmail.com',203847099,'19900206',4)
GO

-----------------------------------------------Datos de los Negocios Afiliados----------------------------------------------------------------------------------
										---------------------DML-------------------

--Se insertan los datos de todos los negocios afiliados
--ID 1
INSERT INTO NEGOCIOS_AFILIADOS(nom_negocio,ced_juridica,direccion,id_distrito)
VALUES('Taco Bell S.A',3101094961,'141 Food Court Plaza Occidente,San Ramon',1)
GO
--ID 2
INSERT INTO NEGOCIOS_AFILIADOS(nom_negocio,ced_juridica,direccion,id_distrito)
VALUES('McDonalds',3101014194,' Plaza Occidente, Los Parques, San Ramón',1)
GO
--ID 3
INSERT INTO NEGOCIOS_AFILIADOS(nom_negocio,ced_juridica,direccion,id_distrito)
VALUES('Taqueria Juan',3101096548,'500mts Sur Escuela Zaragoza, Palmares',3)
GO
--ID 4
INSERT INTO NEGOCIOS_AFILIADOS(nom_negocio,ced_juridica,direccion,id_distrito)
VALUES('Marisqueria Delfin',3101965899,'50mts Norte Abastecedor las Lomas, Palmares',4)
GO
--ID 5
INSERT INTO NEGOCIOS_AFILIADOS(nom_negocio,ced_juridica,direccion,id_distrito)
VALUES('Soda Angel',3101054788,'100mts Oeste del Parque, San Ramon',1)
GO
--ID 6
INSERT INTO NEGOCIOS_AFILIADOS(nom_negocio,ced_juridica,direccion,id_distrito)
VALUES('Rest. Casa Italia',3101078511,'200mts Este Iglesia, San Ramon',2)
GO
--ID 7
INSERT INTO NEGOCIOS_AFILIADOS(nom_negocio,ced_juridica,direccion,id_distrito)
VALUES('Comidas El Che',3101064987,'50mts Norte Redondel, Palmares',3)
GO
--ID 8
INSERT INTO NEGOCIOS_AFILIADOS(nom_negocio,ced_juridica,direccion,id_distrito)
VALUES('Rest. Donde Pata',3101076641,'700mts Norte Hospital, San Ramon',2)--
GO
--ID 9
INSERT INTO NEGOCIOS_AFILIADOS(nom_negocio,ced_juridica,direccion,id_distrito)
VALUES('Pataconeria Milanita',3101037486,'400mts Norte Colegio, Palmares',3)
GO
--ID 10
INSERT INTO NEGOCIOS_AFILIADOS(nom_negocio,ced_juridica,direccion,id_distrito)
VALUES('Rest. Molino',3101037486,'600mts Norte de la estacion de bomberos, Palmares',3)
GO
---------------------------------------------Datos tabla TELEFONOS----------------------------------------------------------------------------------
								---------------------DML---------------------

--Se insertan los datos de todos los numeros de telefono
--Clientes
--ID 1
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('86279004','Celular')
GO

--ID 2
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('84571230','Celular')
GO

--ID 3
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('24530934','Casa')
GO

--ID 4
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('24533658','Casa')
GO

--ID 5
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('84353750','Celular')
GO
--ID 6
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('24459782','Casa')
GO

--ID 7
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('24455423','Casa')
GO
--ID 8
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('84043785','Celular')
GO

--ID 9
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('89136457','Celular')
GO

--ID 10
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('89986577','Celular')
GO

--ID 11
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('24459832','Casa')
GO

--ID 12
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('86363957','Celular')
GO

--ID 13
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('83659368','Celular')
GO 

--ID 14
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('82547401','Celular')
GO 

--ID 15
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('81285743','Celular')
GO
--ID 16
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('83474647','Celular')
GO

--ID 17
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('85464659','Celular')
GO

--ID 18
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('83653893','Celular')
GO

--ID 19
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('87459854','Celular')
GO

--ID 20
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('88755408','Celular')
GO

--ID 21
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('87539859','Celular')
GO
--ID 22
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('85538712','Celular')
GO

--ID 23
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('24528674','Oficina')
GO

--ID 24
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('24522145','Oficina')
GO

--ID 25
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('24527530','Oficina')
GO

--ID 26
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('24521546','Oficina')
GO

--ID 27
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('24529452','Oficina')
GO

--ID 28
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('22572062','Oficina')
GO

--ID 29
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('22572325','Oficina')
GO

--ID 30
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('22579671','Oficina')
GO

--ID 31
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('22572367','Oficina')
GO

--ID 32
INSERT INTO TELEFONOS (num_telefono,tipo_telefono)
VALUES('22574769','Oficina')
GO
-----------------------------------------------Datos tabla TELEFONOS_CLIENTES-----------------------------------------------------------------------------------
										-------------------DML---------------------

--Se insertan los datos de todos los telefonos de los clientes 
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(1,1)
GO
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(2,2)
GO
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(2,3)
GO
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(3,4)
GO
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(3,5)
GO
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(4,6)
GO
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(5,7)
GO
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(6,8)
GO
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(7,9)
GO
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(8,10)
GO
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(9,11)
GO
INSERT INTO TELEFONOS_CLIENTES(id_cliente,id_telefono)
VALUES(10,12)
GO
-------------------------------------------Datos tabla TELEFONOS_AGENTES----------------------------------------------------------------------------------
										--------------DML--------------------

--Se insertan los datos de todos los telefonos de los agentes
INSERT INTO TELEFONOS_AGENTES(id_agente,id_telefono)
VALUES(1,13)
GO
INSERT INTO TELEFONOS_AGENTES(id_agente,id_telefono)
VALUES(2,14)
GO
INSERT INTO TELEFONOS_AGENTES(id_agente,id_telefono)
VALUES(3,15)
GO
INSERT INTO TELEFONOS_AGENTES(id_agente,id_telefono)
VALUES(4,16)
GO
INSERT INTO TELEFONOS_AGENTES(id_agente,id_telefono)
VALUES(5,17)
GO
INSERT INTO TELEFONOS_AGENTES(id_agente,id_telefono)
VALUES(6,18)
GO
INSERT INTO TELEFONOS_AGENTES(id_agente,id_telefono)
VALUES(7,19)
GO
INSERT INTO TELEFONOS_AGENTES(id_agente,id_telefono)
VALUES(8,20)
GO
INSERT INTO TELEFONOS_AGENTES(id_agente,id_telefono)
VALUES(9,21)
GO
INSERT INTO TELEFONOS_AGENTES(id_agente,id_telefono)
VALUES(10,22)
GO

----------------------------------------------Datos tabla TELEFONOS_NEGOCIOS----------------------------------------------------------------------------------
										-----------------DML-----------------------

--Se insertan los datos de todos los telefonos de los negocios
INSERT INTO TELEFONOS_NEGOCIOS(id_negocio,id_telefono)
VALUES(1,23)
GO
INSERT INTO TELEFONOS_NEGOCIOS(id_negocio,id_telefono)
VALUES(2,24)
GO
INSERT INTO TELEFONOS_NEGOCIOS(id_negocio,id_telefono)
VALUES(3,25)
GO
INSERT INTO TELEFONOS_NEGOCIOS(id_negocio,id_telefono)
VALUES(4,26)
GO
INSERT INTO TELEFONOS_NEGOCIOS(id_negocio,id_telefono)
VALUES(5,27)
GO
INSERT INTO TELEFONOS_NEGOCIOS(id_negocio,id_telefono)
VALUES(6,28)
GO
INSERT INTO TELEFONOS_NEGOCIOS(id_negocio,id_telefono)
VALUES(7,29)
GO
INSERT INTO TELEFONOS_NEGOCIOS(id_negocio,id_telefono)
VALUES(8,30)
GO
INSERT INTO TELEFONOS_NEGOCIOS(id_negocio,id_telefono)
VALUES(9,31)
GO
INSERT INTO TELEFONOS_NEGOCIOS(id_negocio,id_telefono)
VALUES(10,32)
GO


----------------------------------------------Datos tabla TIPOS_VEHICULOS-------------------------------------------------------------------------------------
									---------------------DML-------------------

--Se insertan los datos de los tipos de vehiculos
--ID 1
INSERT INTO TIPOS_VEHICULOS(tipo_vehiculo)
VALUES('Carro')
GO
--ID 2
INSERT INTO TIPOS_VEHICULOS(tipo_vehiculo)
VALUES('Moto')
GO
--ID 3
INSERT INTO TIPOS_VEHICULOS(tipo_vehiculo)
VALUES('Bicicleta')
GO

------------------------------------------Datos tabla VEHICULOS-------------------------------------------------------------------------------------
								------------------DML------------------------

--Se insertan los datos de todos los vehiculos 
INSERT INTO VEHICULOS(id_agente,placa,marca,modelo,id_tipo)
VALUES(1,'860559','Toyota','Corolla',1)
GO
INSERT INTO VEHICULOS(id_agente,placa,marca,modelo,id_tipo)
VALUES(2,'643900','Honda','Unicorn',2)
GO
INSERT INTO VEHICULOS(id_agente,placa,marca,modelo,id_tipo)
VALUES(3,NULL,'BIDECA','MTB24',3)
GO
INSERT INTO VEHICULOS(id_agente,placa,marca,modelo,id_tipo)
VALUES(4,'077888','Nissan','Sentra',1)
GO
INSERT INTO VEHICULOS(id_agente,placa,marca,modelo,id_tipo)
VALUES(5,NULL,'RALI','ADVII',3)
GO
INSERT INTO VEHICULOS(id_agente,placa,marca,modelo,id_tipo)
VALUES(6,'547890','Freedom','ZS',2)
GO
INSERT INTO VEHICULOS(id_agente,placa,marca,modelo,id_tipo)
VALUES(7,'711000','Yamaha','FZ150',2)
GO
INSERT INTO VEHICULOS(id_agente,placa,marca,modelo,id_tipo)
VALUES(8,'987436','Daihatsu','Terios',1)
GO
INSERT INTO VEHICULOS(id_agente,placa,marca,modelo,id_tipo)
VALUES(9,'322768','Formula','XRF 200',2)
GO
INSERT INTO VEHICULOS(id_agente,placa,marca,modelo,id_tipo)
VALUES(10,NULL,'Super Pro','MAVERICK',3)
GO


----------------------------------------------Datos tabla ENTREGAS-------------------------------------------------------------------------------------
								--------------------DML------------------

--Se insertan los datos de todos los telefonos de las entregas
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(3,3,1,7,'20211223','10:30:00','Entregado','11:00:00',2.5,5,1.13,'189',3785)
GO
 INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(6,2,2,1,'20211224','12:00:00','Entregado','12:20:00',3,25,1.13,'0',4633)
GO
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(2,2,3,6,'20211225','15:00:00','Pendiente','00:00:00',4,18,1.13,'0',6328)
GO
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(10,3,4,4,'20211226','13:00:00','Entregado','13:07:00',1,3,1.13,'0',1243)
GO
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(4,1,5,2,'20211227','16:00:00','Entregado','16:20:00',12,35,1.13,'932',19888)
GO
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(5,3,6,3,'20211227','16:55:00','Entregado','17:04:00',1.5,2,1.13,'104',2090)
GO
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(7,2,7,9,'20211228','11:00:00','Pendiente','11:15:00',10,16,1.13,'0',16498)
GO
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(1,1,8,2,'20211229','10:05:00','Entregado','10:35:00',13,20,1.13,'0',21583)
GO
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(8,1,9,3,'20211230','14:25:00','Entregado','14:50:00',11,17,1.13,'909',18193)
GO
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(9,2,10,5,'20211231','13:00:00','Entregado','13:12:00',12,17,1.13,'0',19888)
GO


--------------------------------------------Datos tabla SALARIOS_AGENTES-------------------------------------------------------------------------------------
									------------------DML-----------------------

--Se insertan los datos de los salarios de los agentes
INSERT INTO SALARIOS_AGENTES(id_agente,fecha_salarios,salario_bruto,carga_social,rebajo_vehiculo,rebajo_aplicacion,salario_neto)
VALUES(1,'20211230',100000,10.5,0.02,0.09,79625)
GO
INSERT INTO SALARIOS_AGENTES(id_agente,fecha_salarios,salario_bruto,carga_social,rebajo_vehiculo,rebajo_aplicacion,salario_neto)
VALUES(2,'20211230',100000,10.5,0.02,0.09,79625)
GO
INSERT INTO SALARIOS_AGENTES(id_agente,fecha_salarios,salario_bruto,carga_social,rebajo_vehiculo,rebajo_aplicacion,salario_neto)
VALUES(3,'20211230',100000,10.5,0.00,0.07,83424)
GO
INSERT INTO SALARIOS_AGENTES(id_agente,fecha_salarios,salario_bruto,carga_social,rebajo_vehiculo,rebajo_aplicacion,salario_neto)
VALUES(4,'20211230',100000,10.5,0.02,0.09,80557)
GO
INSERT INTO SALARIOS_AGENTES(id_agente,fecha_salarios,salario_bruto,carga_social,rebajo_vehiculo,rebajo_aplicacion,salario_neto)
VALUES(5,'20211230',100000,10.5,0.00,0.07,83339)
GO
INSERT INTO SALARIOS_AGENTES(id_agente,fecha_salarios,salario_bruto,carga_social,rebajo_vehiculo,rebajo_aplicacion,salario_neto)
VALUES(6,'20211230',100000,10.5,0.02,0.09,79625)
GO
INSERT INTO SALARIOS_AGENTES(id_agente,fecha_salarios,salario_bruto,carga_social,rebajo_vehiculo,rebajo_aplicacion,salario_neto)
VALUES(7,'20211230',100000,10.5,0.02,0.09,79856)
GO
INSERT INTO SALARIOS_AGENTES(id_agente,fecha_salarios,salario_bruto,carga_social,rebajo_vehiculo,rebajo_aplicacion,salario_neto)
VALUES(8,'20211230',100000,10.5,0.02,0.09,80534)
GO
INSERT INTO SALARIOS_AGENTES(id_agente,fecha_salarios,salario_bruto,carga_social,rebajo_vehiculo,rebajo_aplicacion,salario_neto)
VALUES(9,'20211230',100000,10.5,0.02,0.09,79625)
GO
INSERT INTO SALARIOS_AGENTES(id_agente,fecha_salarios,salario_bruto,carga_social,rebajo_vehiculo,rebajo_aplicacion,salario_neto)
VALUES(10,'20221230',100000,10.5,0.00,0.07,83235)
GO

----------------------------------------------------------------DML---------------------------------------------------------------

--Insercion de nuevas entregas
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(8,1,6,7,'20220101','14:00:00','Entregado','14:10:00',10,23,1.13,'0',16498)
GO
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(3,3,3,6,'20220101','15:20:00','Entregado','16:20:00',2,5,1.13,'0',8023)
GO
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(1,1,8,8,'20220102','10:50:00','Entregado','11:07:00',7,28,1.13,'0',11413)
GO
INSERT INTO ENTREGAS(id_agente,id_tipo_vehiculo,id_cliente,id_negocio,fecha,hora_entrada_entrega,estado_entrega,hora_entregado,distancia_entrega,peso_paquete,impuesto,bono,total_pago)
VALUES(7,2,7,7,'20220103','12:40:00','Entregado','12:45:00',3,18,1.13,'231',4633)
GO

--Insecion de un nuevo canton
INSERT INTO CANTONES(nom_canton,id_provincia)
VALUES('Naranjo',1)
GO
--Insecion de un nuevo distrito
INSERT INTO DISTRITOS(nom_distrito,id_canton) 
VALUES('San Miguel',7)
GO
--Insecion de un nuevo negocio que se ubica en el canton de Naranjo
INSERT INTO NEGOCIOS_AFILIADOS(nom_negocio,ced_juridica,direccion,id_distrito)
VALUES('Rest.Manolos',31010495,'800mts Norte de repuestos El Buen Carrito',10)
GO
--Actualizacion de un dato de un cliente
UPDATE CLIENTES
SET correo_electronico = 'carljimen_12@gmail.com'
WHERE ced_cliente = 208660215

--Actualizacion de un dato de un negocio
UPDATE NEGOCIOS_AFILIADOS
SET direccion = '750mts Norte de repuestos El Buen Carrito'
WHERE ced_juridica = '31010495'

