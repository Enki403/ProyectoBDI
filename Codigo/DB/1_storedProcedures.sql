/**
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 7/12/2020
*/

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
DROP PROCEDURE IF EXISTS sp_initialize$$
CREATE PROCEDURE sp_initialize()
BEGIN
    -- *Insertar usuario administrador
    INSERT INTO User(bit_admin, blo_name, blo_password) VALUES (1, AES_ENCRYPT("admin", @key), AES_ENCRYPT("admin", @key));

    -- *Insertar valores de configuracion
    INSERT INTO Config(blo_penColorValue, blo_fillColorValue) VALUES (AES_ENCRYPT("#000000", @key), AES_ENCRYPT("#000000", @key));

    -- *autentication, visualization, creation, modification o elimination.
    INSERT INTO Activity(var_name) VALUES ("Autentication"), ("Visualization"), ("Creation"), ("Modification"), ("Elimination");

END$$

/**
 * !SP createUser
 * * Registra a un usuario, necesita como parametro nombre y contraseña
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 5/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_createUser$$
CREATE PROCEDURE sp_createUser(
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
DROP PROCEDURE IF EXISTS sp_deleteUser$$
CREATE PROCEDURE sp_deleteUser(
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
DROP PROCEDURE IF EXISTS sp_getUsers$$
CREATE PROCEDURE sp_getUsers()
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
 * * Modifica el nombre de un usuario de OLD_NOMBRE a NOMBRE exceptuando al administrador
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 6/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_modifyUserName$$
CREATE PROCEDURE sp_modifyUserName(
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
 * * Modifica la contraseña por PASS del usuario NOMBRE exceptuando al administrador
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 6/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_modifyUserPass$$
CREATE PROCEDURE sp_modifyUserPass(
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
            INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 4, CONCAT("User's ('", NOMBRE, "') password has been updated.")); 
        END IF;
    END IF;
END$$

/**
 * !SP getLogbook
 * * Obtiene el los datos de la bitacora
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 6/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_getLogbook$$
CREATE PROCEDURE sp_getLogbook()
BEGIN
    -- * Obtiene todos los resultados de  la bitacora
    SELECT Logbook.id AS "id", 
           AES_DECRYPT(User.blo_name, @key) AS "User Name",
           Activity.var_name AS "Action", 
           Logbook.tex_description AS "Description", 
           Logbook.dat_creationDate AS "Creation Date" 
    FROM Logbook, User, Activity
    WHERE Logbook.id_user = User.id AND Logbook.id_activity = Activity.id;
END$$
/**
 * !SP getConfig
 * * Obtiene el los datos de la configuracion de pen color y fill color
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 7/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_getConfig$$
CREATE PROCEDURE sp_getConfig()
BEGIN
    -- * Obtiene los registros de configuracion
    SELECT AES_DECRYPT(blo_penColorValue, @key) AS "Pen Color Value", 
           AES_DECRYPT(blo_fillColorValue, @key) AS "Fill Color Value"
    FROM Config;
    INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 2, CONCAT("Pen Color and Fill Color has been seen.")); 
END$$
/**
 * !SP setConfig
 * * Cambia los datos de ppen color y fill color
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 7/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_setConfig$$
CREATE PROCEDURE sp_setConfig(
    IN PEN VARCHAR(7),
    IN FILL VARCHAR(7))
BEGIN
    -- * modifica los registros de configuracion
    UPDATE Config 
            SET blo_penColorValue = AES_ENCRYPT(PEN, @key),
                blo_fillColorValue = AES_ENCRYPT(FILL, @key)
            WHERE id = 1;
    IF ROW_COUNT() = 1 THEN
        INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 4, CONCAT("Congiguration values has been updated.")); 
    END IF;
END$$

/**
 * !SP userAuthenticated
 * * Obtiene el nombre de todos los usuarios
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 6/12/2020
 * @version 1
 */
 DROP PROCEDURE IF EXISTS sp_userAuthenticated$$
CREATE PROCEDURE sp_userAuthenticated(
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

/**
 * !SP createDrawing
 * * Crea un dibujo en la base de datos. USERID representa el id del usuario que guarda, NOMBRE representa el nombre del dibujo, DRAWDATA representa el json
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 5/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_createDrawing$$
CREATE PROCEDURE sp_createDrawing(
    IN USERID TEXT, 
    IN NOMBRE TEXT, 
    IN DRAWDATA TEXT)
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

    -- * Inserta dibujo a la base de datos
    INSERT INTO Drawing(id_user, blo_name, blo_blob) VALUES 
        (USERID, AES_ENCRYPT(NOMBRE, @key), AES_ENCRYPT(DRAWDATA, @key));
    IF ROW_COUNT() = 1 THEN
        INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (USERID, 3, CONCAT("Drawing '", NOMBRE, "' has been created."));
    END IF;
END$$

DELIMITER ;