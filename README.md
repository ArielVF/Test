# test
API REST
Para el uso correcto de la API REST creada se deben tener en cuenta las siguientes consideraciones:
1. Los datos deben estar contenidos en mockAPI, allí, los agentes deben contar con los atributos "nombre" y "clave", mientras
que las incidencias deben tener como atributos "Fecha", "Titulo", "Descripcion" y "Agente". Tal cual se escribe en las comillas,
respetando mayúsculas y ausencia de tildes.
2. Dentro del código, si hubiese problemas con el link de mockAPI que va establecido (contiene los datos de las pruebas aplicadas)
se debe actualizar por alguno que esté funcionando y respete la estructura del punto 1. Aquí, solo se debe agregar la dirección en
el código fuente, en la variable url1 (para incidencias) y url2 (para agentes). En el script también debe actualizarse la url, por la que
contenga los datos de incidencias.
3.Si llega a haber alguna falla al momento de ejecución, verificar que el entorno en donde se esté ejecutando el programa contenga las 
últimas versiones de las librerias o elementos importados en el código.
4. La búsqueda de incidencias por fechas y agentes funciona de la siguiente forma:
- Para el caso de las fechas, debe ser el número de la fecha sin guiones ni barras. Ejemplo: localhost:4000/issues/15052020  
. El comando anterior, retorna las incidencias de la fecha 15/05/2020.
- El segundo caso, solo basta con escribir el nombre tal cual se guardó. Ejemplo: localhost:4000/issues/ariel valenzuela  
. El comando anterior retorna la incidencias registradas por Ariel Valenzuela.
5. Para el registro, se ha creado el endpoint /login. Es un método post que mediante un authorization de postman acepta un usuario y clave,
si estos coinciden con usuario de los registrados entregará un token, éste token se debe agregar en un header de postman que estrictamente
se debe llamar "access-token", y es éste el que permite el ingreso al endpoint /issue, para la creación de incidencias.
6. En el endpoint /issue el atributo "Agente" es obviado, debido a que se toma como agente aquella persona que se encuentra registrada. Por lo 
tanto, aunque se ingrese un agente laT incidencia se almacena con el nombre del usuario que ha ingresado al endpoint.

- Código principal Apirest.py
. Teniendo en cuenta las consideraciones, la ejecución es sencilla, a través de una terminal se ejecuta el código (en visual code es 
python nombre_programa.py), éste iniciará y arrancará de manera local en el puerto 4000. Luego, mediante postman se puede comenzar a 
ejecutar las peticiones. Cuando se envían datos mediante post (endpoint /agent e /issue) se debe respetar el formato json.

- Código script script.py
. Para la ejecución del script que genera incidencias se debe ejecutar en otra terminal, este script solcita un título y una descripción
de la incidencia a registrar, luego toma la fecha actual y la registra en el campo "Fecha". El agente por defecto queda como "Python script agente".
