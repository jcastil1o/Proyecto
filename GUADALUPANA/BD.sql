CREATE SCHEMA GUADALUPANA;
CREATE TABLE IF NOT EXISTS `GUADALUPANA`.`datos`
(
	`id_datos` INT AUTO_INCREMENT,
	`CUI` INT NOT NULL,
    `Nombre` VARCHAR(20),
    `Apellido` VARCHAR(20),
    `Direccion` VARCHAR(100),
    `Telefono` VARCHAR(20),
    `Plaza` VARCHAR(35),
    PRIMARY KEY (id_datos),
    CONSTRAINT CUI FOREIGN KEY (CUI)
    REFERENCES GUADALUPANA.Escolaridad(CUI)
);

CREATE TABLE IF NOT EXISTS `GUADALUPANA`.`Escolaridad`
(
	`id_esc` INT,
	`CUI` INT NOT NULL,
    `Grado` TEXT NOT NULL,
    PRIMARY KEY (CUI)
);
CREATE TABLE IF NOT EXISTS `GUADALUPANA`.`pruebas`
(
            id INT AUTO_INCREMENT PRIMARY KEY,
            Mensaje LONGTEXT,
            Tiempo TIMESTAMP
);
SELECT * FROM  `GUADALUPANA`.`datos`;
SELECT * FROM  `GUADALUPANA`.`Escolaridad`;
SELECT * FROM `GUADALUPANA`.`pruebas`;
SELECT 
	datos.id_datos, datos.CUI, datos.Nombre, datos.Plaza
FROM `GUADALUPANA`.`datos` 
INNER JOIN `GUADALUPANA`.`Escolaridad` 
ON datos.CUI = Escolaridad.CUI;
