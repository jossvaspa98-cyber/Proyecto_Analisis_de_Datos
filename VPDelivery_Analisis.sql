INSERT INTO TiposVehiculos (descripcion)
VALUES 
('Moto'),
('Bicicleta'),
('Automóvil'),
('Camioneta'),
('Scooter');


INSERT INTO Agentes (nombre, correo, fecha_nacimiento)
VALUES 
('Luis Mora', 'luis.mora@vpdelivery.com', '1990-01-10'),
('Ana Soto', 'ana.soto@vpdelivery.com', '1993-03-15'),
('Carlos Ruiz', 'carlos.ruiz@vpdelivery.com', '1985-06-20'),
('María Vargas', 'maria.vargas@vpdelivery.com', '1991-04-05'),
('David Pérez', 'david.perez@vpdelivery.com', '1996-08-25'),
('Karen Jiménez', 'karen.jimenez@vpdelivery.com', '1992-02-17'),
('Josue Rodríguez', 'josue.rodriguez@vpdelivery.com', '1989-09-13'),
('Daniela Campos', 'daniela.campos@vpdelivery.com', '1995-11-30'),
('Esteban Quesada', 'esteban.quesada@vpdelivery.com', '1994-10-01'),
('Lucía Gamboa', 'lucia.gamboa@vpdelivery.com', '1987-05-12'),
('Andrés Mena', 'andres.mena@vpdelivery.com', '1990-07-07'),
('Laura Picado', 'laura.picado@vpdelivery.com', '1993-12-11'),
('Felipe Mora', 'felipe.mora@vpdelivery.com', '1986-03-09'),
('Juliana Rojas', 'juliana.rojas@vpdelivery.com', '1997-01-28'),
('Javier Campos', 'javier.campos@vpdelivery.com', '1995-06-06'),
('Rebeca Vega', 'rebeca.vega@vpdelivery.com', '1992-10-20'),
('Mauricio Solís', 'mauricio.solis@vpdelivery.com', '1991-03-19'),
('Tatiana Chaves', 'tatiana.chaves@vpdelivery.com', '1994-04-14'),
('Ricardo Brenes', 'ricardo.brenes@vpdelivery.com', '1996-09-09'),
('Sofía Navarro', 'sofia.navarro@vpdelivery.com', '1993-07-25');


INSERT INTO Clientes (nombre, direccion, correo)
VALUES 
('Pedro Gómez', 'Av. Central #45', 'pedro.gomez@mail.com'),
('Laura Ramírez', 'Calle 9 #123', 'laura.ramirez@mail.com'),
('Carlos Fernández', 'Barrio Escalante', 'carlos.fer@mail.com'),
('Lucía Herrera', 'San Pedro Este', 'lucia.herrera@mail.com'),
('Luis Vargas', 'Av. 2da #50', 'luis.vargas@mail.com'),
('Silvia Jiménez', 'Residencial Lomas', 'silvia.j@mail.com'),
('Mario Quesada', 'Guadalupe Oeste', 'mario.q@mail.com'),
('Patricia Arias', 'Desamparados Centro', 'patricia.arias@mail.com'),
('Fernando Rojas', 'Santa Ana Norte', 'fernando.rojas@mail.com'),
('Natalia Marín', 'Curridabat #10', 'natalia.m@mail.com'),
('Daniel Castro', 'Alajuelita', 'daniel.castro@mail.com'),
('Johana Sequeira', 'Tres Ríos', 'johana.s@mail.com'),
('Erick Navarro', 'Moravia', 'erick.n@mail.com'),
('Gabriela Soto', 'La Unión', 'gabriela.soto@mail.com'),
('Jose Rodríguez', 'San Antonio', 'jose.r@mail.com'),
('Alejandra Mata', 'Paso Ancho', 'alejandra.mata@mail.com'),
('Cristian Chaves', 'Barrio México', 'cristian.ch@mail.com'),
('Isabel Vega', 'Hatillo 5', 'isabel.v@mail.com'),
('Oscar Méndez', 'Rohrmoser', 'oscar.mendez@mail.com'),
('Melissa Cordero', 'Escazú', 'melissa.cordero@mail.com');



INSERT INTO Vehiculos (id_agente, tipo_id, placa, marca, modelo)
VALUES 
(1, 1, 'A123BC', 'Yamaha', 'XTZ125'),
(2, 2, 'B234CD', 'Giant', 'Escape 3'),
(3, 3, 'C345DE', 'Toyota', 'Yaris'),
(4, 1, 'D456EF', 'Suzuki', 'AX100'),
(5, 4, 'E567FG', 'Nissan', 'NP300'),
(6, 2, 'F678GH', 'Specialized', 'Sirrus'),
(7, 1, 'G789HI', 'Honda', 'CBR250'),
(8, 5, 'H890IJ', 'Xiaomi', 'Mi Scooter'),
(9, 4, 'I901JK', 'Hyundai', 'Tucson'),
(10, 3, 'J012KL', 'Chevrolet', 'Aveo'),
(11, 2, 'K123LM', 'Trek', 'FX 2'),
(12, 1, 'L234MN', 'Bajaj', 'Boxer'),
(13, 5, 'M345NO', 'Segway', 'Ninebot'),
(14, 3, 'N456OP', 'Kia', 'Picanto'),
(15, 4, 'O567PQ', 'Ford', 'Ranger'),
(16, 1, 'P678QR', 'Suzuki', 'GN125'),
(17, 2, 'Q789RS', 'Scott', 'Speedster'),
(18, 4, 'R890ST', 'Isuzu', 'D-Max'),
(19, 3, 'S901TU', 'Mazda', '2'),
(20, 5, 'T012UV', 'Okai', 'Neon');



INSERT INTO Entregas (id_agente, id_cliente, id_vehiculo, fecha, hora_inicio, hora_fin, estado, distancia_km, peso_kg, total_pago)
VALUES 
(1, 1, 1, '2025-12-01', '08:00', '08:30', 'Entregado', 5.4, 2.1, 1200),
(2, 2, 2, '2025-12-01', '09:15', '10:00', 'Entregado', 10.2, 3.4, 1800),
(3, 3, 3, '2025-12-02', '07:30', '08:05', 'Entregado', 3.5, 1.2, 900),
(4, 4, 4, '2025-12-02', '10:00', NULL, 'Pendiente', 12.0, 5.0, 0),
(5, 5, 5, '2025-12-03', '11:30', '12:00', 'Entregado', 6.0, 2.8, 1400),
(6, 6, 6, '2025-12-03', '12:15', NULL, 'Pendiente', 8.7, 3.3, 0),
(7, 7, 7, '2025-12-04', '09:00', '09:45', 'Entregado', 4.8, 2.5, 1100),
(8, 8, 8, '2025-12-04', '13:00', '13:30', 'Entregado', 7.9, 4.2, 1700),
(9, 9, 9, '2025-12-05', '14:00', NULL, 'Pendiente', 6.5, 1.9, 0),
(10, 10, 10, '2025-12-05', '15:30', '16:00', 'Entregado', 2.4, 1.0, 800),
(11, 11, 11, '2025-12-06', '08:00', '08:30', 'Entregado', 5.2, 3.3, 1150),
(12, 12, 12, '2025-12-06', '09:15', '10:00', 'Entregado', 6.9, 2.9, 1250),
(13, 13, 13, '2025-12-07', '10:30', NULL, 'Pendiente', 9.1, 4.8, 0),
(14, 14, 14, '2025-12-07', '11:45', '12:20', 'Entregado', 3.3, 1.5, 980),
(15, 15, 15, '2025-12-08', '12:30', '13:00', 'Entregado', 7.7, 2.0, 1600),
(16, 16, 16, '2025-12-08', '13:30', '14:10', 'Entregado', 4.5, 2.6, 1000),
(17, 17, 17, '2025-12-09', '14:15', NULL, 'Pendiente', 8.0, 5.1, 0),
(18, 18, 18, '2025-12-09', '15:00', '15:45', 'Entregado', 10.3, 3.8, 1850),
(19, 19, 19, '2025-12-10', '07:45', '08:20', 'Entregado', 5.6, 2.7, 1300),
(20, 20, 20, '2025-12-10', '08:30', NULL, 'Pendiente', 6.0, 3.2, 0);




