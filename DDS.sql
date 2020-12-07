/**
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 5/12/2020
*/

DROP DATABASE IF EXISTS DrawingApp;
CREATE DATABASE DrawingApp CHARACTER SET utf8;
USE DrawingApp;

--* Procedimientos Almacenados
DELIMITER $$

--* Contraseña de encriptado
SET @key = "admin";

/**
 * !SP Inicialize
 * * 'Inicializa' la base de datos con los valores iniciales correspondientes.
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 5/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS initialize$$
CREATE PROCEDURE initialize()
BEGIN
    -- *Insertar usuario administrador
    INSERT INTO User(bit_admin, blo_name, blo_password) VALUES (1, AES_ENCRYPT("admin", @key), AES_ENCRYPT("admin", @key));

    -- *Insertar valores de configuracion
    INSERT INTO Config(blo_penColorValue, blo_fillColorValue) VALUES (AES_ENCRYPT("#000000", @key), AES_ENCRYPT("#000000", @key));

    -- *autentication, visualization, creation, modification o elimination.
    INSERT INTO Activity(var_name) VALUES ("Autentication"), ("Visualization"), ("Creation"), ("Modification"), ("Elimination");

END$$

/**
 * !SP registerUser
 * * Registra a un usuario, necesita como parametro nombre y contraseña
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 5/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS registerUser$$
CREATE PROCEDURE registerUser(
    IN NOMBRE TEXT, 
    IN PASS TEXT)
BEGIN
    -- * Maneja el error de modo que retorne un json eg. { errno: 1062, msg: Duplicate entry} si existe algun problema.
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1 
            @sqlState = RETURNED_SQLSTATE, 
            @errno = MYSQL_ERRNO, 
            @msgText = MESSAGE_TEXT;
        SET @full_error = CONCAT("{ errno: ",@errno,", msg: ",SUBSTRING(@msgText,1,15) ,"}");
        SELECT @full_error AS "ERROR";
    END;
    -- * Inserta al usuario a la base de datos
    INSERT INTO User(blo_name, blo_password) VALUES (AES_ENCRYPT(NOMBRE, @key), AES_ENCRYPT(PASS, @key));
    IF ROW_COUNT() = 1 THEN
        INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 3, CONCAT("User '", NOMBRE, "' created."));
    END IF;
END$$

/**
 * !SP deleteUser
 * * Elimina al usuario de la base de datos, excepto al administrador
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 6/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS deleteUser$$
CREATE PROCEDURE deleteUser(
    IN NOMBRE TEXT)
BEGIN
    -- * Maneja el error de modo que retorne un json eg. { errno: 1062, msg: Duplicate entry} si existe algun problema.
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1 
            @sqlState = RETURNED_SQLSTATE, 
            @errno = MYSQL_ERRNO, 
            @msgText = MESSAGE_TEXT;
        SET @full_error = CONCAT("{ errno: ",@errno,", msg: ",@msgText,"}");
        SELECT @full_error AS "ERROR";
    END;
    -- * Borra al usuario de la base de datos solo si no es el administrador
    IF 'admin' != NOMBRE THEN
        DELETE FROM User WHERE AES_DECRYPT(blo_name, @key) = NOMBRE;
        IF ROW_COUNT() = 1 THEN
            INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 5, CONCAT("User '", NOMBRE, "' deleted."));
        END IF;
    END IF;
END$$

/**
 * !SP getUsers
 * * Obtiene el nombre de todos los usuarios exceptuando del administrador
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 6/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS getUsers$$
CREATE PROCEDURE getUsers()
BEGIN
    -- * Maneja el error de modo que retorne un json eg. { errno: 1062, msg: Duplicate entry} si existe algun problema.
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1 
            @sqlState = RETURNED_SQLSTATE, 
            @errno = MYSQL_ERRNO, 
            @msgText = MESSAGE_TEXT;
        SET @full_error = CONCAT("{ errno: ",@errno,", msg: ",@msgText,"}");
        SELECT @full_error AS "ERROR";
    END;
    -- * Obtiene todos los usuarios
    SELECT id AS "id", AES_DECRYPT(blo_name, @key) AS "Name", AES_DECRYPT(blo_password, @key) AS "Password", AES_DECRYPT(blo_creationDate, @key) AS "Creation Date", AES_DECRYPT(blo_modificationDate, @key) AS "Modification Date" FROM User  WHERE  AES_DECRYPT(blo_name, @key) != 'admin';
END$$

/**
 * !SP modifyUserName
 * * Modifica el nombre de un usuario de OLD_NOMBRE a NOMBRE
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 6/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS modifyUserName$$
CREATE PROCEDURE modifyUserName(
    IN OLD_NOMBRE TEXT,
    IN NOMBRE TEXT)
BEGIN
    -- * Maneja el error de modo que retorne un json eg. { errno: 1062, msg: Duplicate entry} si existe algun problema.
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1 
            @sqlState = RETURNED_SQLSTATE, 
            @errno = MYSQL_ERRNO, 
            @msgText = MESSAGE_TEXT;
        SET @full_error = CONCAT("{ errno: ",@errno,", msg: ",SUBSTRING(@msgText,1,15) ,"}");
        SELECT @full_error AS "ERROR";
    END;
    -- * Modifica el usuario que concuerde con el parametro
    UPDATE User 
        SET blo_name = AES_ENCRYPT(NOMBRE, @key),
            blo_modificationDate = AES_ENCRYPT(NOW(), @key)
        WHERE blo_name = AES_ENCRYPT(OLD_NOMBRE, @key);
    IF ROW_COUNT() = 1 THEN
        INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 4, CONCAT("User with name '", OLD_NOMBRE, "' updated to '", NOMBRE,"'."));
    END IF;
END$$

/**
 * !SP modifyUserPass
 * * Modifica el nombre de un usuario de OLD_NOMBRE a NOMBRE
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 6/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS modifyUserPass$$
CREATE PROCEDURE modifyUserPass(
    IN NOMBRE TEXT,
    IN PASS TEXT)
BEGIN
    -- * Maneja el error de modo que retorne un json eg. { errno: 1062, msg: Duplicate entry} si existe algun problema.
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1 
            @sqlState = RETURNED_SQLSTATE, 
            @errno = MYSQL_ERRNO, 
            @msgText = MESSAGE_TEXT;
        SET @full_error = CONCAT("{ errno: ",@errno,", msg: ",@msgText," }");
        SELECT @full_error AS "ERROR";
    END;
    -- * Modifica el usuario que concuerde con el parametro
    IF 'admin' != NOMBRE THEN
        UPDATE User 
            SET blo_password = AES_ENCRYPT(PASS, @key),
                blo_modificationDate = AES_ENCRYPT(NOW(), @key)
            WHERE blo_name = AES_ENCRYPT(NOMBRE, @key);
        IF ROW_COUNT() = 1 THEN
            INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 4, CONVERT(CONCAT("User's ('", NOMBRE, "') password has been updated.") USING UTF8)); 
        END IF;
    END IF;
END$$

/**
 * !SP getLogbook
 * * Obtiene el nombre de todos los usuarios exceptuando del administrador
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 6/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS getLogbook$$
CREATE PROCEDURE getLogbook()
BEGIN
    -- * Maneja el error de modo que retorne un json eg. { errno: 1062, msg: Duplicate entry} si existe algun problema.
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1 
            @sqlState = RETURNED_SQLSTATE, 
            @errno = MYSQL_ERRNO, 
            @msgText = MESSAGE_TEXT;
        SET @full_error = CONCAT("{ errno: ",@errno,", msg: ",@msgText,"}");
        SELECT @full_error AS "ERROR";
    END;
    -- * Obtiene todos los resultados de 
    SELECT Logbook.id AS "id", 
           AES_DECRYPT(User.blo_name, @key) AS "User Name",
           Activity.var_name AS "Action", 
           Logbook.tex_description AS "Description", 
           Logbook.dat_creationDate AS "Creation Date" 
    FROM Logbook, User, Activity
    WHERE Logbook.id_user = User.id AND Logbook.id_activity = Activity.id;
END$$

/**
 * !SP authLog
 * * Obtiene el nombre de todos los usuarios
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 6/12/2020
 * @version 1
 */
 DROP PROCEDURE IF EXISTS authLog$$
CREATE PROCEDURE authLog(
    IN NOMBRE TEXT)
BEGIN
    -- * Maneja el error de modo que retorne un json eg. { errno: 1062, msg: Duplicate entry} si existe algun problema.
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1 
            @sqlState = RETURNED_SQLSTATE, 
            @errno = MYSQL_ERRNO, 
            @msgText = MESSAGE_TEXT;
        SET @full_error = CONCAT("{ errno: ",@errno,", msg: ",@msgText,"}");
        SELECT @full_error AS "ERROR";
    END;
    -- * Se agrega un registro a la bitacora
    INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 1, CONCAT("User ('", NOMBRE, "') has been authenticated."));
END$$

DELIMITER ;

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


--* Inicializacion de base de datos
CALL initialize();
