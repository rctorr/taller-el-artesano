![talleres de python](./el-artesano.jpg)
# Proyecto de Programación Computacional

## Objetivos

- Aumentar las espectativas escolares de los adolescentes
- Dotar a los adolescentes de herramientas computacionales que les permita tener mejores oportunidades
- Dotar de un pensamiénto crítico y analítico
- Formar a nuevos usuarios e impulsores de la cultura libre y el software libre.
- Fometar una actitud de investigación y desarrollo

## Contenido propuesto

### Sesión 1: Indroducción
- Conociendo el software libre, super poderes para tu computadora
- Definiendo el "código de conducta"
- ¿Qué es la programación?
- Comunicándonos con la computadora
- Instalando Python
- Conociendo Python (La serpiente mágica pero no inteligente!)

[Ver más ...](./introduccion.ipynb)

### Sesión 2: La red social de programadores Git y GitHub
- Instalando Notepad++
- Descripción de editor de código
- Instalando Git
- Conociendo la consola
- Trabajando ejemplos con Git

### Sesión 3: Programación en la ciencias
#### Preparando carpeta de trabajo
- Creando carpeta ejemplos-python/
- Cambiarse a esa carpeta ejemplos-python/
- Crear archivo hola.py con notepadd++
- Guardarlo dentro en:
    ```
    ejemplos-python/
        |- hola.py
    ```
- Inicializar repo de git con: git init
- Configurar nuestro nombre e email en git con:
    $ git config --global user.name "Ricardo Torres"
    $ git config --global user.email rictor@cuhrt.com
- Agregar cambios con: git add hola.py
- Guardar cambos con: git commit -m "Iniciando proyecto"
- Registrarse en GitHub y entrar con su nuevo usuario
- Crear el repo con el nombre: ejemplos-python
- Enlazar el repo de GitHub con nuestra carpeta local
    - Copiando la dirección del repo en GitHub
    - Pegarla en la consola con el comando
        $ git remote add origin <pegar texto aquí>
    - Actualizando el repo en GitHub con:
        $ git pull -u origin master
- Verificar que nuestros archivos están en GitHub

*Ejercicio:*
- Modificar hola.py para que escriba 10 veces el mensaje "Hola Git!"
- Agregar los cambios a git
- Guardar los cambios en git local
- Enviar los cambios a GitHub
- Terminas cuando se puedan ver los cambios en la página de GitHub

#### Calculando el área de un cuadrado
![](./ejecutando-nuestro-programa.png)
- Instalando PilasEngine
- Conociendo PilasEngine
- Creando un programa para calcular el área de un cuadrado llamado area-de-cuadrado.py
- Escribir el siguiente código
![](./calcula-area-cuadrado.png)

- Verificar que funcione bien y que los resultados son correctos
- Agregar cambios a git con: git add area-de-cuadrado.py
- Guardar cambios a git con: git commit -m "Agregando programa area de un cuadrado"
- Guardar cambios a github con: git push origin master

*Ejercicio:*
- Crear un programa llamado volumen-de-cubo.py para calcular el volumen de un cubo
- Verificar que funcione de forma correcta
- Agregar cambios a git con: git add volumen-de-cubo.py
- Guardar cambios a git con: git commit -m "Agregando programa volumen de un cubo"
- Guardar cambios a github con: git push origin master
- Terminas cuando tu programa funcionando se pueda ver en la página de GitHub

### Sesión 4: Programación en las ciencias humanas y de expresión
- Creando una aplicación que detecte faltas de ortografía y/o proporcione la regla gramatical correspondiente (programación modular)

### Sesión 5: La producción de un vídeo juego
- Definición del juego
- Bosquejo del funcionamiento
- Definición de actores, acciones, reglas, leyes físicas, químicas, biológicas o sociales que afectarán al juego.
- Definición de módulos
- Definición de los datos
- Definición de las reglas
- Programación o desarrolo
- Pruebas de la versión alpha
- Programación y corrección de errores
- Pruebas de la versión beta
- Programación y corrección de más errores
- Lanzamiento de la versión 1.0
- Corrección de errores
- Lanzamiento de la versión 1.1
- ...
- Revisemos un libro...

## Recursos

* Python: http://python.org
* Tutorial introductorio a python: http://www.learnpython.org/es
