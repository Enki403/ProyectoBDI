Documentación de Análisis
=====
IS501 Base de Datos I
-----
Proyecto Final
-----
### **Programa de Dibujo Elaborado en Python con Librería Tkinter:**
#### Descripción General
- El proyecto consiste en un programa de dibujo elaborado en python
extraído del libro Data Structures and Algorithms, a partir de el cual
se debe reemplazar los datos que utilizan XML, por uso de JSON y almacenamiento en una
base de datos A y una de respaldo B con compresión mediante python3 y linux. Adicionalmente, se agrega al sistema un módulo de autenticación, un módulo de registros de bitácora, una pantalla para creación, modificación y eliminación de usuarios.

### Authors:
- Héctor José Vásquez López 
    - 20171004509
- Nelson Jafet Sambula Palacios 
    - 20161032207
- Luis Gerardo Gutiérrez Perdomo 
    - 20161005902
- Renata Mavelyn Dubón Madrid 
    - 20171000808

**Bitácora de Trabajo**
-----

### Día 0:
- El equipo se reúne por video conferencia para discutir, analizar, comprender y estructurar el proyecto, aportando ideas, conceptos, análisis previos, críticas y sugerencias en conjunto con el objetivo de definir tareas entre los integrantes del equipo, identificar las dificultades o retos que representa la asignación y establecer los primeros avances gráficos que servirán para la documentación de análisis del mismo.
- Se transcribe el código python usando la librería tkinter extraído del libro de Data Structures and Algorithms.

### Día 1:
- Se elabora el esquema entidad relación del problema planteado. Inicial. Este fue mejorado en el día 1.
- Se ilustra el flujo identificado de las ventanas necesarias de las que constará el proyecto. Esto mediante una imagen que muestra el flujo de ventanas, adjunta en la carpeta de documentación del proyecto.
- Se elaboran los mockups de las ventanas de las que constará el proyecto.
- Se logra realizar el parseo del XML generado por el programa con tkinter a un formato JSON.

### Día 2:
- Se analiza la estructura de la base de datos de la siguiente manera:
    - Entidades:
        - User: Debe haber un usuario administrador ya que se debe encriptar los datos con la clave o contraseña del administrador por lo que no puede haber más, ya que no puede haber más de una llave de encriptación.
        - Drawing
        - Bitácora: Como atributoa tendría una descripción de la acción y si un dibujo fue modificado o involucrado o un usuario y/o su configuración.
        - Acción: Ya sea autenticación, visualización, creación o modificación, eliminación. 
        - Configuración: se piensa que contendrá solamente un registro modificable por el usuario administrador. Se está considerando que se introduzca un historial de registros y que el actual sea el último registro guardado en la tabla, o tener sólo uno que se vaya modificando (actualizando con update). Surge inclinación por la primera opción para que la base de datos no llegue a ser tan grande.
        
*Diagrama ER inicial.*  
![Diagrama ER Inicial](https://i.pinimg.com/originals/7a/8b/2d/7a8b2dd4ff6276f920dbba8dbf5aa65b.jpg) 

### Día 3:
- Se empieza a diseñar procedimientos almacenados para almacenar o registrar usuarios.
- Surge problema al encriptar, dado a incompatibilidad de tipos de variables, ya que no se puede almacenar un varchar en un tipo text, sino que se debe usar el tipo de dato BLOB.
- Se descubre que la función AES Encrypt retorna un tipo de dato BLOB o más bien información que debe ser guardada en un BLOB. 
- Se estrablece que se debe cambiar los tipos de datos a tipo BLOB para que no exista ya el problema de encriptación.
- Se establecen mejoras en el diagrama ER que se diseñó el día anterior.
- Se diseña el Modelo Relacional.
 
*Diagrama ER final.*  
![Diagrama ER Final](https://i.pinimg.com/originals/dd/4c/cf/dd4ccf82b478dc60c0359c59e46a6516.png) 

*Modelo relacional.*  
![Modelo Relacional](https://i.pinimg.com/originals/fe/ac/99/feac992f7435f2cce83e1dfa7ac9acd7.png)

### Día 4:
- Se analiza cómo el código extraído del libro Data Structures and Algorithms, va guardando los datos del dibujo resultante, ya que para eso, a la hora de construir la ventana de dibujo, hay una función que observa, que se pasa a otra función que se ejecuta cada vez, escuchando cada cambio que tenga, cada movimiento de puntero, llamada ontrack. Cada vez que se dispara esta función esta guarda los registros del dibujo, y acciones realizadas con el mouse como dibujar con el mouse, levantar el pincel, bajar el pincel, seleccionar color, seleccionar color de relleno, cualquier acción referente al dibujo. Inicialmente se guardaba en un String con formato XML.
- Se realiza cambio para que la salida del programa de dibujo no sea XML, sino una llave y un valor de tipo JSON. Por ejemplo si se hace un traslado de un pixel a otro, este dibujo se guardará como datos de posición en X, en Y, el color, el tipo de comando, todo se guarda en una llave que contendrá cada uno de estos valores, en una variable llamada graphicComand que guarda todo el contenido de estas llaves.
### Día 5:
- Se logra realizar un parseo cada vez que el usuario realice una acción. Se recorre el contenido del String que genera el programa y se parsea para convertirlo en un objeto JSON. A la hora de cargar el contenido del JSON, se realiza un proceso de parseo del contenido del BLOB a JSON y convertirlo al contenido original, decodificado del dibujo.
- Se fragmenta el código extraído del libro, se pone en un sólo archivo las funciones de las acciones, agregar, eliminar, descargar, configuración, salir. En otro archivo las configuraciones de herramientas de dibujo, cambiar color, el ancho, el radio. Y otro archivo con los comandos, guarda el comando que se esté ejecutando en la ventana de dibujo y la propiedad respectiva, como posición en X, Y, color, ancho, radio, esto dependiendo de qué herramienta esté usando el usuario operador.

### Día 6
- Se analiza el flujo de la aplicación, la manera en que se comportarán las ventanas.
- Se diseñan las ventanas que tendrá la aplicación. Se diseñaron conforme a QT5 y la aplicación de dibujo extraída del libro Data Structures and Algorithms utiliza la librería tkinter.
- A medida avanza el trabajo, el equipo se ve en la necesidad de cambiar de librería QT5 a tkinter, todas las ventanas del programa, a excepción de la ventana de login, que permanecerá utilizando la librería QT5, mientras que los menús de configuración y load se diseñan con tkinter.

*Diagrama de flujo de ventanas.*  
![Flujo de ventanas](https://i.pinimg.com/originals/1a/8e/00/1a8e00eb338e4c43db979eee45d4bec3.jpg)

### Día 7:
- Se quiere hacer una vista para obtener los registros de la bitácora y de los usuarios.
- Se falla al tratar de utilizar una vista, debido a que hay que utilizar una variable, y en las vistas no se pueden
utilizar estas.
- Se toma la decisión de diseñar un procedimiento almacenado que devuelva la tabla que se requiere para obtener los registros de la bitácora y de los usuarios.

### Día 8:
- Se realiza el CRUD de los usuarios, en donde se agrega la funcionalidad de editar, eliminar y añadir usuarios, mediante los botones de la ventana de edición de usuarios disponible solo para el usuario administrador.
- Se inicia la configuración del archivo "config.init".
- Se trata de mejorar la implementación del archivo "config.init", para que funcione de una manera más adecuada.

### Día 9:
- Se terminan algunos métodos elaborados en python para las siguientes tareas:
    - initialize: se ejecuta una sóla vez en todo el programa. Inserta el usuario administrador a la base de datos, más específicamente a la tabla de usuarios. Inserta las configuraciones iniciales de la tabla config, en las columnas de penColor y fillColor, con los valores de #0000. Inicializa las actividades del CRUD, autenticación, visualización, creación, modificación y eliminación. Se piensa insertar esto en el run, para que no sea un procedimiento almacenado.
    - createUser: se utiliza para la creación de usuarios, recibe como parámetros el nombre y la contraseña del nuevo usuario. Contiene un control de repitencia. Si el nombre ya existe, no inserta el nuevo usuario. Retorna un JSON con el número de error y el mensaje cuando esto sucede.Se realizó así por facilidad a la hora de trabajar y extraer datos de JSON. La mayoría de los métodos funcionan de esta manera. Al ocurrir un error se retorna el JSON que contiene dicho error.
    - insertUser: se inserta el usuario a la base de datos. Si se realiza correctamente, se escribe en la bitácora que el usuario se ingresó correctamente, como un nuevo registro de esta tabla.
    - deleteUSer: sirve para eliminar un usuario. Como parámetro sólo recibe el nombre del usuario a eliminar. Si el usuario se elimina correctamente de la tabla de usuarios, se escribe eso en la bitácora como un nuevo registro. Sino, se retorna el JSON con el respectivo error. El admin es el único usuario que no puede ser eliminado.

### Día 10:
- Se terminan algunos métodos elaborados en python para las siguientes tareas:
    - getUsers: se utiliza para obtener toda la tabla de usuarios ya desencriptada. Muestra todos los usuarios exceptuando al usuario administrador. Esto con el fin de tratar de evitar intentos de eliminar al admin, los cuales terminarían lanzando un error.
    - modifyUsername: se utiliza para modificar el nombre dle usuario actual. Como parámetros recibe el nombre actual del usuario a modificar y el nombre nuevo que se le dará a este. Tiene la misma verificación de repitencia que la función createUser. Si hay alguien con el mismo nombre, no se realiza el cambio de nombre y retorna el JSON con el respectivo error. Si el cambio es exitoso, modifica la fecha de moificación del registro, y cambia el nombre actual del usuario por el nuevo nombre, luego se ingresa un nuevo registro a la bitácora conteniendo esta información de actividad.
    - modifyUserpass: modifica el password del usuario. Recibe como parámetros el nombre del usuario y la nueva contraseña a asignar a dicho usuario.Se puede modificar la contraseña de todo los usuarios menos la del usuario administrador, ya que esta contrasñea sirve para la encriptación de los datos.

### Día 11:
- Se terminan algunos métodos elaborados en python para las siguientes tareas:
    - getLogBook: función que se usa para obtener todos los registros de la bitácora.
    - getConfig: sirve para obtener los valores de la configuración actual de los campos penColor y fillColor.
    - setConfig: sirve para actualizar o modificar los valores del primer y único registro de esa tabla de configuración, cuyos campos son penColor y fillColor. Si el cambio es exitoso, se registra la actividad en la bitácora.
    - userAuthenticated: cuando el usuario realiza el login o ingreso al programa con su nombre y contraseña, se llama a esta función para registrar la actividad de login en la bitácora.
    - createDrawing: función de prueba, aún no aprobada. Como parámetros recibe el nombre de usuario creador del dibujo, su ID y el JSON con DrawData. Se piensa que debe haber una variable de estado dentro del programa, que contenga la información del usuario que se encuentra loggeado actualmente en el programa.

### Día 12:
- La bitácora empieza a funcionar desde el login.
- Se realiza el parseo, al guardar un dibujo, se convierte el JSON que contiene su información, a datos binarios y se envía a la base de datos. Al cargar, se paresea el contenido binario a JSON con datos decodificables para el programa, para que estos  puedan ser mostrados como el gráfico del dibujo.

### Día 13:
- Se realiza la conexión entre la interfaz y la base de datos, mediante el llamado de procesos almacenados. Se empezó por el login, luego "agregar dibujo", "cargar dibujo", el CRUD de usuarios.

### Día 14:
- Se activa la funcionalidad del botón "descargar". Cuando este es persionado, se descargan los datos del dibujo que fue cargado por última vez en el programa. Si al iniciar la aplicación este botón es presionado, se lanza un mensaje de error, ua que no hay un dibujo que haya sido cargado, es decir, no hay dibujos guardados en la base de datos B. Esto se debe a que cuando se carga un dibujo, se guarda el ID de ese dibujo, y si se quiere descargar, entonces se busca en la base de datos B, el dibujo que coincida con el ID requerido.