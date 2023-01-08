DESCRIPCION GENERAL DEL PROYECTO
Este proyecto final consiste en una página para poder cargar posteos. Estos posteos contienen un titulo, subtitulo y descripción. A su vez, se le puede incorporar una imágen y la fecha en la que se realizó el posteo. Esto está definido en el modelo Post en models.py. 

El objetivo principial de la página es poder compartir lugares del mundo que vale la pena visitar por eso la app se llama conoce_lugares.

Los posts y su detalle lo puede ver cualquier persona que ingrese en el url de nombre= "conoce-lugares-index", a su vez podran ingresar al about en donde explico brevemente quien soy y por qué creé la página y a Contacto para poder enviar un mensaje, colocando email, nombre y texto (detallado en el modelo Mensaje en models.py). Sin embargo, para poder cargar, modificar o borrar (CRUD) un posteo uno debe registrarse y solicitar acceso de staff. Este acceso se configura en el url 'admin'.

La funcionalidad del CRUD queda definida en views.py con las clases PostCrear, PostActualizar y PostBorrar.

Por otro lado, al crear un usuario se le puede colocar un avatar que lo represente. Una vez colocado se podrá actualizar presionando el hipervincluo Actualizar Avatar en el url con nombre="conoce-lugares-listar". Esta funcionalidad del avatar se puede ver en models.py en el modelo Avatar (donde se especifica que la imagen que se define como avatar se asocie a un usuario) y en views.py en la clase AvatarActualizar (permitiendo el cambio en el campo imagen).

STATUS DEL PROYECTO
El proyecto se encuentra terminado, es decir, el crud, el signup y el login/logout funciona correctamente. Igualmente, me gustaría poder incursionar más en el diseño de la página, poder corregir imperfecciones, colores y tipo de letra. 

INSTRUCCIONES
Antes de probar en el explorador como funciona la app hay que correr el servidor escribiendo en la terminal py manage.py runserver. Una vez ejecutado ese paso, ingrear al link que figura en los comentarios de la terminal para que se abra una pantalla con los urls declarados. 

REPOSITORIO DE GITHUB
https://github.com/julietabarrios/proyecto-final.git


