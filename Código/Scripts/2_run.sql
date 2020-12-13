/**
 * @author hjvasquez@unah.hn
 * @author nelson.sambula@unah.hn
 * @author lggutierrez@unah.hn
 * @author renata.dubon@unah.hn
 * @date 12/12/2020
*/

source 0_tables_A.sql
source 0_tables_B.sql
source 1_storedProcedures_A.sql

USE DrawingApp;

-- * Inicializacion de base de datos
CALL sp_initialize();