/**
 * @author Hector Jose Vasquez Lopez <hjvasquez@unah.hn>
 * @date 7/12/2020
*/

source 0_tables.sql
source 1_storedProcedures.sql


USE DrawingApp;

-- * Inicializacion de base de datos
CALL sp_initialize();


-- * Datos de Prueba

-- * ingresando usuarios
CALL sp_createUser("Hector", "123asd");
CALL sp_createUser("Renata", "123asd");
CALL sp_createUser("Luis", "123asd");
CALL sp_createUser("Nelson", "123asd");
CALL sp_createUser("Jean", "123asd");
CALL sp_createUser("Henry", "123asd");

-- * ingresando dibujos
CALL sp_createDrawing(2, "Dibujo 1", '{"data":"testData"}');
CALL sp_createDrawing(2, "Dibujo 2", '{"data":"testData"}');
CALL sp_createDrawing(2, "Dibujo 3", '{"data":"testData"}');
CALL sp_createDrawing(3, "Dibujo", '{"data":"testData"}');
CALL sp_createDrawing(3, "Dibujos", '{"data":"testData"}');
CALL sp_createDrawing(4, "Dibujoslocos", '{"data":"testData"}');