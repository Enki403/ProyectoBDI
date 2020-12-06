DROP DATABASE IF EXISTS DrawingApp;
CREATE DATABASE DrawingApp CHARACTER SET utf8;
USE DrawingApp;

/**
 * TODO: PASAR TODAS LAS VARIABLES A TIPO BLOB PARA PODER ENCRIPTARLAS CON AES_ENCRYPT()
*/

-- Procedimiento Almacenado
DELIMITER $$

SET @key = "admin";

/*
DROP PROCEDURE IF EXISTS initialize$$

CREATE PROCEDURE initialize()
BEGIN
    -- Insertar usuario administrador
    INSERT INTO User(bit_admin, tex_name, tex_password) VALUES (1, AES_ENCRYPT("admin",@key), AES_ENCRYPT("admin",@key));

    -- Insertar valores de configuracion
    INSERT INTO Config(var_penColorValue, var_fillColorValue) VALUES (AES_ENCRYPT("#000000",@key), AES_ENCRYPT("#000000",@key));

    -- autentication, visualization, creation, modification o elimination.
    INSERT INTO Activity(var_name) VALUES (AES_ENCRYPT("Autentication",@key)), (AES_ENCRYPT("Visualization",@key)), (AES_ENCRYPT("Creation",@key)), (AES_ENCRYPT("Modification",@key)), (AES_ENCRYPT("Elimination",@key));

END$$
*/

DROP PROCEDURE IF EXISTS registerUser$$

CREATE PROCEDURE registerUser(IN NOMBRE TEXT, IN PASS TEXT)
BEGIN
    INSERT INTO User(tex_name, tex_password) VALUES (AES_ENCRYPT(NOMBRE, @key), PASS);

END$$

DELIMITER ;

-- Creacion de tablas

DROP TABLE IF EXISTS Activity;
CREATE TABLE Activity(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Identificador unico de una actividad.",
    var_name VARCHAR(13) NOT NULL COMMENT "Nombre de la actividad."
) COMMENT "Tabla de actividades Puede ser autentication, visualization, creation, modification o elimination.";

DROP TABLE IF EXISTS Config;
CREATE TABLE Config(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Identificador unico de la configuracion inicial",
    var_penColorValue VARCHAR(7) NOT NULL COMMENT "Valor inicial de pen color.",
    var_fillColorValue VARCHAR(7) NOT NULL COMMENT "Valor inicial de fill color."
) COMMENT "Tabla de configuracion inicial";

DROP TABLE IF EXISTS User;
CREATE TABLE User(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Identificador unico de User.",
    bit_admin BIT NOT NULL DEFAULT 0 COMMENT "Si es administrador es 1, de lo contrario 0.",
    tex_name BLOB NOT NULL UNIQUE COMMENT "Nombre del usuario.",
    tex_password TEXT NOT NULL COMMENT "Contraseña del usuario.",
    dat_creationDate DATETIME NOT NULL DEFAULT NOW() COMMENT "Fecha en la que el usuario fue creado.",
    dat_modificationDate DATETIME NOT NULL DEFAULT NOW() COMMENT "Fecha en la que el usuario fue modificado."
) COMMENT "Tabla de usuarios";

DROP TABLE IF EXISTS Drawing;
CREATE TABLE Drawing(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Identificador unico del.",
    id_user INT NOT NULL COMMENT "LLave foranea que hace referencia a un usuario.",
    tex_name TEXT NOT NULL UNIQUE COMMENT "Nombre del dibujo.",
    jso_blob JSON NOT NULL COMMENT "Contiene el dibujo",
    dat_creationDate DATETIME NOT NULL DEFAULT NOW() COMMENT "Fecha en la que el dibujo fue creado.",
    dat_modificationDate DATETIME NOT NULL DEFAULT NOW() COMMENT "Fecha en la que el dibujo fue modificado.",
    FOREIGN KEY ( id_user ) REFERENCES User(id)
        ON DELETE CASCADE ON UPDATE CASCADE
) COMMENT "Tabla de dibujos";

DROP TABLE IF EXISTS Logbook;
CREATE TABLE Logbook(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Identificador unico de Logbook.",
    id_user INT NOT NULL COMMENT "LLave foranea que hace referencia a un usuario.",
    id_activity INT NOT NULL COMMENT "LLave foranea que hace referencia a una actividad.",
    tex_description TEXT NOT NULL COMMENT "Descripcion de lo que el usaurio ha realizado.",
    dat_creationDate DATETIME NOT NULL DEFAULT NOW() COMMENT "Fecha en la que el usuario realizo la accion.",
    FOREIGN KEY ( id_user ) REFERENCES User(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY ( id_activity ) REFERENCES Activity(id)
        ON DELETE CASCADE ON UPDATE CASCADE
) COMMENT "Tabla de bitacora";



-- Insertar usuario administrador
INSERT INTO User(bit_admin, tex_name, tex_password) VALUES (1, AES_ENCRYPT("admin", "admin"), "admin");

-- Insertar valores de configuracion
INSERT INTO Config(var_penColorValue, var_fillColorValue) VALUES ("#000000", "#000000");

-- autentication, visualization, creation, modification o elimination.
INSERT INTO Activity(var_name) VALUES ("Autentication"),
                                      ("Visualization"),
                                      ("Creation"),
                                      ("Modification"),
                                      ("Elimination");
