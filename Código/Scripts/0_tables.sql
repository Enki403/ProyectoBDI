/**
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 7/12/2020
*/

DROP DATABASE IF EXISTS DrawingApp;
CREATE DATABASE DrawingApp CHARACTER SET utf8;
USE DrawingApp;

--* Creacion de tablas
DROP TABLE IF EXISTS Config;
CREATE TABLE Config(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Identificador unico de la configuracion inicial",
    blo_penColorValue BLOB NOT NULL COMMENT "Valor inicial de pen color.",
    blo_fillColorValue BLOB NOT NULL COMMENT "Valor inicial de fill color."
) COMMENT "Tabla de configuracion inicial";

DROP TABLE IF EXISTS User;
CREATE TABLE User(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Identificador unico de User.",
    bit_admin BIT NOT NULL DEFAULT 0 COMMENT "Si es administrador es 1, de lo contrario 0.",
    blo_name BLOB NOT NULL UNIQUE COMMENT "Nombre del usuario.",
    blo_password BLOB NOT NULL COMMENT "Contraseña del usuario.",
    blo_creationDate BLOB NOT NULL DEFAULT AES_ENCRYPT(NOW(), "admin") COMMENT "Fecha en la que el usuario fue creado.",
    blo_modificationDate BLOB NOT NULL DEFAULT AES_ENCRYPT(NOW(), "admin") COMMENT "Fecha en la que el usuario fue modificado."
) COMMENT "Tabla de usuarios";

DROP TABLE IF EXISTS Drawing;
CREATE TABLE Drawing(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Identificador unico del.",
    id_user INT NOT NULL COMMENT "LLave foranea que hace referencia a un usuario.",
    blo_name BLOB NOT NULL UNIQUE COMMENT "Nombre del dibujo.",
    blo_blob BLOB NOT NULL COMMENT "Contiene el dibujo",
    blo_creationDate BLOB NOT NULL DEFAULT AES_ENCRYPT(NOW(), "admin") COMMENT "Fecha en la que el dibujo fue creado.",
    blo_modificationDate BLOB NOT NULL DEFAULT AES_ENCRYPT(NOW(), "admin") COMMENT "Fecha en la que el dibujo fue modificado.",
    FOREIGN KEY ( id_user ) REFERENCES User(id)
        ON DELETE CASCADE ON UPDATE CASCADE
) COMMENT "Tabla de dibujos";

DROP TABLE IF EXISTS Activity;
CREATE TABLE Activity(
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT "Identificador unico de una actividad.",
    var_name VARCHAR(13) NOT NULL COMMENT "Nombre de la actividad."
) COMMENT "Tabla de actividades Puede ser autentication, visualization, creation, modification o elimination.";

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