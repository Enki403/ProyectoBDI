/**
 * @author hjvasquez@unah.hn
 * @author nelson.sambula@unah.hn
 * @author lggutierrez@unah.hn
 * @author renata.dubon@unah.hn
 * @date 12/12/2020
*/

USE DrawingApp;

--* Procedimientos Almacenados
DELIMITER $$

--* Contraseña de encriptado
SET @key = "admin";

/**
 * !SP Inicialize
 * * 'Inicializa' la base de datos con los valores iniciales correspondientes.
 * @date 5/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_initialize$$
CREATE PROCEDURE sp_initialize()
BEGIN
    -- *Insertar usuario administrador
    IF (SELECT count(*) FROM User) = 0 THEN
        INSERT INTO User(bit_admin, blo_name, blo_password) VALUES (1, AES_ENCRYPT("admin", @key), AES_ENCRYPT("admin", @key));
        INSERT INTO DrawingAppBackup.User(bit_admin, blo_name, blo_password) VALUES (1, AES_ENCRYPT("admin", @key), AES_ENCRYPT("admin", @key));
    END IF;
    -- *Insertar valores de configuracion
    IF (SELECT count(*) FROM Config) = 0 THEN
        INSERT INTO Config(blo_penColorValue, blo_fillColorValue) VALUES (AES_ENCRYPT("#000000", @key), AES_ENCRYPT("#000000", @key));
        INSERT INTO DrawingAppBackup.Config(blo_penColorValue, blo_fillColorValue) VALUES (AES_ENCRYPT("#000000", @key), AES_ENCRYPT("#000000", @key));
    END IF;

    -- *autentication, visualization, creation, modification o elimination.
    IF (SELECT count(*) FROM Activity) = 0 THEN
        INSERT INTO Activity(var_name) VALUES ("Autentication"), ("Visualization"), ("Creation"), ("Modification"), ("Elimination");
        INSERT INTO DrawingAppBackup.Activity(var_name) VALUES ("Autentication"), ("Visualization"), ("Creation"), ("Modification"), ("Elimination");
    END IF;

END$$

/**
 * !SP createUser
 * * Registra a un usuario, necesita como parametro nombre y contraseña
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
    INSERT INTO User(blo_name, blo_password) VALUES (AES_ENCRYPT(NOMBRE, "admin"), AES_ENCRYPT(PASS, "admin"));
    IF ROW_COUNT() = 1 THEN
        INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 3, CONCAT("User '", NOMBRE, "' created."));
    END IF;
    INSERT INTO DrawingAppBackup.User(blo_name, blo_password) VALUES (AES_ENCRYPT(NOMBRE, "admin"), AES_ENCRYPT(PASS, "admin"));
    IF ROW_COUNT() = 1 THEN
        INSERT INTO DrawingAppBackup.Logbook(id_user, id_activity, tex_description) VALUES (1, 3, CONCAT("User '", NOMBRE, "' created."));
    END IF;
END$$

/**
 * !SP deleteUser
 * * Elimina al usuario de la base de datos y todos sus dibujos, excepto al administrador
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
        DELETE FROM User WHERE AES_DECRYPT(blo_name, "admin") = NOMBRE;
        IF ROW_COUNT() = 1 THEN
            INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 5, CONCAT("User '", NOMBRE, "' deleted with all its drawings."));
        END IF;
        DELETE FROM DrawingAppBackup.User WHERE AES_DECRYPT(blo_name, "admin") = NOMBRE;
        IF ROW_COUNT() = 1 THEN
            INSERT INTO DrawingAppBackup.Logbook(id_user, id_activity, tex_description) VALUES (1, 5, CONCAT("User '", NOMBRE, "' deleted with all its drawings."));
        END IF;
    END IF;
END$$

/**
 * !SP getUsers
 * * Obtiene el nombre de todos los usuarios exceptuando del administrador
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
    SELECT id AS "id", AES_DECRYPT(blo_name, "admin") AS "Name", AES_DECRYPT(blo_password, "admin") AS "Password", AES_DECRYPT(blo_creationDate, "admin") AS "Creation Date", AES_DECRYPT(blo_modificationDate, "admin") AS "Modification Date" FROM User  WHERE  AES_DECRYPT(blo_name, "admin") != 'admin';
END$$

/**
 * !SP getUserId
 * * Obtiene el id del usaurio
 * @date 6/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_getUserId$$
CREATE PROCEDURE sp_getUserId(
    IN NOMBRE TEXT
)
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
    SELECT id AS "id" FROM User  WHERE blo_name = AES_ENCRYPT(NOMBRE, "admin");
END$$

/**
 * !SP modifyUserName
 * * Modifica el nombre de un usuario de OLD_NOMBRE a NOMBRE exceptuando al administrador
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
        SET blo_name = AES_ENCRYPT(NOMBRE, "admin"),
            blo_modificationDate = AES_ENCRYPT(NOW(), "admin")
        WHERE blo_name = AES_ENCRYPT(OLD_NOMBRE, "admin");
    IF ROW_COUNT() = 1 THEN
        INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 4, CONCAT("User with name '", OLD_NOMBRE, "' updated to '", NOMBRE,"'."));
    END IF;
    UPDATE DrawingAppBackup.User 
        SET blo_name = AES_ENCRYPT(NOMBRE, "admin"),
            blo_modificationDate = AES_ENCRYPT(NOW(), "admin")
        WHERE blo_name = AES_ENCRYPT(OLD_NOMBRE, "admin");
    IF ROW_COUNT() = 1 THEN
        INSERT INTO DrawingAppBackup.Logbook(id_user, id_activity, tex_description) VALUES (1, 4, CONCAT("User with name '", OLD_NOMBRE, "' updated to '", NOMBRE,"'."));
    END IF;
END$$

/**
 * !SP modifyUserPass
 * * Modifica la contraseña por PASS del usuario NOMBRE exceptuando al administrador
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
            SET blo_password = AES_ENCRYPT(PASS, "admin"),
                blo_modificationDate = AES_ENCRYPT(NOW(), "admin")
            WHERE blo_name = AES_ENCRYPT(NOMBRE, "admin");
        IF ROW_COUNT() = 1 THEN
            INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 4, CONCAT("User's ('", NOMBRE, "') password has been updated.")); 
        END IF;
        UPDATE DrawingAppBackup.User 
            SET blo_password = AES_ENCRYPT(PASS, "admin"),
                blo_modificationDate = AES_ENCRYPT(NOW(), "admin")
            WHERE blo_name = AES_ENCRYPT(NOMBRE, "admin");
        IF ROW_COUNT() = 1 THEN
            INSERT INTO DrawingAppBackup.Logbook(id_user, id_activity, tex_description) VALUES (1, 4, CONCAT("User's ('", NOMBRE, "') password has been updated.")); 
        END IF;
    END IF;
END$$

/**
 * !SP getLogbook
 * * Obtiene el los datos de la bitacora
 * @date 6/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_getLogbook$$
CREATE PROCEDURE sp_getLogbook()
BEGIN
    -- * Obtiene todos los resultados de  la bitacora
    SELECT Logbook.id AS "id", 
           AES_DECRYPT(User.blo_name, "admin") AS "User Name",
           Activity.var_name AS "Action", 
           Logbook.tex_description AS "Description", 
           Logbook.dat_creationDate AS "Creation Date" 
    FROM Logbook, User, Activity
    WHERE Logbook.id_user = User.id AND Logbook.id_activity = Activity.id ORDER BY Logbook.id;
END$$
/**
 * !SP getConfig
 * * Obtiene el los datos de la configuracion de pen color y fill color
 * @date 7/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_getConfig$$
CREATE PROCEDURE sp_getConfig()
BEGIN
    -- * Obtiene los registros de configuracion
    SELECT AES_DECRYPT(blo_penColorValue, "admin") AS "Pen Color Value", 
           AES_DECRYPT(blo_fillColorValue, "admin") AS "Fill Color Value"
    FROM Config;
    INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 2, CONCAT("Pen Color and Fill Color has been seen.")); 
END$$
/**
 * !SP setConfig
 * * Cambia los datos de ppen color y fill color
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
            SET blo_penColorValue = AES_ENCRYPT(PEN, "admin"),
                blo_fillColorValue = AES_ENCRYPT(FILL, "admin")
            WHERE id = 1;
    IF ROW_COUNT() = 1 THEN
        INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 4, CONCAT("Configuration values has been updated.")); 
    END IF;
    -- * modifica los registros de configuracion b
    UPDATE DrawingAppBackup.Config 
            SET blo_penColorValue = AES_ENCRYPT(PEN, "admin"),
                blo_fillColorValue = AES_ENCRYPT(FILL, "admin")
            WHERE id = 1;
    IF ROW_COUNT() = 1 THEN
        INSERT INTO DrawingAppBackup.Logbook(id_user, id_activity, tex_description) VALUES (1, 4, CONCAT("Configuration values has been updated.")); 
    END IF;
END$$

/**
 * !SP userAuthenticated
 * * Obtiene el nombre de todos los usuarios
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
    -- * Se agrega un registro a la bitacora b
    INSERT INTO DrawingAppBackup.Logbook(id_user, id_activity, tex_description) VALUES (1, 1, CONCAT("User ('", NOMBRE, "') has been authenticated."));
END$$

/**
 * !SP createDrawing
 * * Crea un dibujo en la base de datos. USERID representa el id del usuario que guarda, NOMBRE representa el nombre del dibujo, DRAWDATA representa el json
 * @date 7/12/2020
 * @version 1
 */
 -- TODO: sobreescribir los datos si el dibujo existe.
DROP PROCEDURE IF EXISTS sp_createDrawing$$
CREATE PROCEDURE sp_createDrawing(
    IN USERID TEXT, 
    IN NOMBRE TEXT, 
    IN DRAWDATA LONGTEXT)
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
        (USERID, AES_ENCRYPT(NOMBRE, "admin"), AES_ENCRYPT(DRAWDATA, "admin"));
    IF ROW_COUNT() = 1 THEN
        INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (USERID, 3, CONCAT("Drawing '", NOMBRE, "' has been created by ", (SELECT AES_DECRYPT(User.blo_name, "admin") FROM User WHERE User.id = USERID),"."));
    END IF;
    -- * Inserta dibujo a la base de datos b
    INSERT INTO DrawingAppBackup.Drawing(id_user, blo_name, blo_blob) VALUES 
        (USERID, AES_ENCRYPT(NOMBRE, "admin"), AES_ENCRYPT(DRAWDATA, "admin"));
    IF ROW_COUNT() = 1 THEN
        INSERT INTO DrawingAppBackup.Logbook(id_user, id_activity, tex_description) VALUES (USERID, 3, CONCAT("Drawing '", NOMBRE, "' has been created by ", (SELECT AES_DECRYPT(User.blo_name, "admin") FROM User WHERE User.id = USERID),"."));
    END IF;
END$$

/**
 * !SP deleteDrawing
 * * Elimina un dibujo en la base de datos. NOMBRE representa el nombre del dibujo
 * @date 8/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_deleteDrawing$$
CREATE PROCEDURE sp_deleteDrawing(
    IN USERID TEXT,
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

    -- * Elimina dibujo a la base de datos
    DELETE FROM Drawing WHERE AES_DECRYPT(blo_name, "admin") = NOMBRE;
    IF ROW_COUNT() = 1 THEN
        INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (USERID, 5, CONCAT("Drawing '", NOMBRE, "' has been deleted by ", (SELECT AES_DECRYPT(User.blo_name, "admin") FROM User WHERE User.id = USERID),"."));
    END IF;
    -- * Elimina dibujo a la base de datos b
    DELETE FROM DrawingAppBackup.Drawing WHERE AES_DECRYPT(blo_name, "admin") = NOMBRE;
    IF ROW_COUNT() = 1 THEN
        INSERT INTO DrawingAppBackup.Logbook(id_user, id_activity, tex_description) VALUES (USERID, 5, CONCAT("Drawing '", NOMBRE, "' has been deleted by ", (SELECT AES_DECRYPT(User.blo_name, "admin") FROM User WHERE User.id = USERID),"."));
    END IF;
END$$

/**
 * !SP getDrawings
 * * Obtiene el nombre de todos los dibujos
 * @date 8/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_getDrawings$$
CREATE PROCEDURE sp_getDrawings()
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
    -- * Obtiene todos los dibujos
    SELECT Drawing.id AS "id", AES_DECRYPT(User.blo_name, "admin") AS "User", AES_DECRYPT(Drawing.blo_name, "admin") AS "Name"  FROM Drawing, User WHERE Drawing.id_user = User.id;
END$$

/**
 * !SP getDrawingsByUser
 * * Obtiene el nombre de todos los dibujos de un usuario en especifico
 * @date 8/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_getDrawingsByUser$$
CREATE PROCEDURE sp_getDrawingsByUser(
    IN USERID INT
)
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
    -- * Obtiene todos los dibujos
    SELECT Drawing.id AS "id", AES_DECRYPT(User.blo_name, "admin") AS "User", AES_DECRYPT(User.blo_modificationDate, "admin") AS "Date",AES_DECRYPT(Drawing.blo_name, "admin") AS "Name"  FROM Drawing, User WHERE USERID = Drawing.id_user AND USERID = User.id GROUP BY Drawing.id;
END$$

/**
 * !SP getSketch
 * * Obtiene los la informacion de un dibujo en especifico.
 * @date 8/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_getSketch$$
CREATE PROCEDURE sp_getSketch(
    IN USERID TEXT,
    IN DRAWINGID TEXT)
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
    IF (SELECT count(*) FROM Drawing WHERE id_user = USERID)>0 THEN
        -- * Obtiene todos los dibujos
        SELECT id AS "id", AES_DECRYPT(blo_name, "admin") AS "Name", AES_DECRYPT(blo_blob, "admin") AS "Drawing Data" FROM Drawing WHERE id = DRAWINGID;
        INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 2, CONCAT("Drawing '", DRAWINGID, "' has been seen by ", (SELECT AES_DECRYPT(User.blo_name, "admin") FROM User WHERE User.id = USERID),"."));
    ELSE
        SELECT CONCAT('{ "errno": 3, "msg": "This user has no drawings yet."}') AS "ERROR";
    END IF;
END$$

/**
 * !SP getSketchDownload
 * * Obtiene los la informacion de un dibujo en especifico.
 * @date 8/12/2020
 * @version 1
 */
DROP PROCEDURE IF EXISTS sp_getSketchDownload$$
CREATE PROCEDURE sp_getSketchDownload(
    IN DRAWID INT
)
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
    IF (SELECT count(*) FROM DrawingAppBackup.Drawing WHERE id = DRAWID)>0 THEN
        -- * Obtiene el dibujo de la base de datos de respaldo
        SELECT AES_DECRYPT(blo_blob, "admin") AS "Drawing Data", AES_DECRYPT(blo_name, "admin") AS "Name" FROM DrawingAppBackup.Drawing WHERE id = DRAWID;
        -- todo CAMBIAR LA ACTIVIDAD EN LA BITACORA
        INSERT INTO Logbook(id_user, id_activity, tex_description) VALUES (1, 2, CONCAT("Drawing ", DRAWID," has been seen by ."));
    ELSE
        SELECT CONCAT('{ "errno": 3, "msg": "This user has no drawings yet."}') AS "ERROR";
    END IF;
END$$

DELIMITER ;
