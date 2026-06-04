# BasicTkinterCalculator

## Descripción
Este es un proyecto de calculadoras que incluye una calculadora básica de escritorio desarrollada en Python utilizando la biblioteca Tkinter para la interfaz gráfica de usuario y una calculadora web construida con Flask. Ambas calculadoras permiten realizar operaciones matemáticas básicas como suma, resta, multiplicación y división.

## Tecnologías Utilizadas
- **Python**: Lenguaje de programación utilizado para desarrollar la lógica de ambas calculadoras.
- **Tkinter**: Biblioteca estándar de Python para la creación de interfaces gráficas de usuario en la calculadora de escritorio.
- **Flask**: Microframework de Python utilizado para crear la aplicación web de la calculadora.

## Esquema de Base de Datos
Este proyecto no utiliza una base de datos, por lo que esta sección no aplica.

## Cómo Correr el Proyecto

### Calculadora de Escritorio
1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/Rayfel2/BasicTkinterCalculator
    ```
3. Navega al directorio del proyecto:
    ```bash
    cd BasicTkinterCalculator
    ```
4. Ejecuta el archivo principal de la calculadora de escritorio:
    ```bash
    python calculadora.py
    ```

### Calculadora Web
1. Asegúrate de tener Python y Flask instalados en tu sistema. Puedes instalar Flask usando el siguiente comando:
    ```bash
    pip install Flask
    ```
2. Clona este repositorio en tu máquina local si no lo has hecho aún:
    ```bash
    git clone https://github.com/Rayfel2/BasicTkinterCalculator
    ```
3. Navega al directorio del proyecto:
    ```bash
    cd BasicTkinterCalculator
    ```
4. Ejecuta el archivo principal de la aplicación web:
    ```bash
    python app.py
    ```
5. Abre tu navegador web y accede a `http://127.0.0.1:5000` para utilizar la calculadora web de manera local. Vas a obtener esta página: https://www.intec.edu.do/

## Cómo Correr el Comando de Pruebas
1. Asegúrate de tener Python instalado en tu sistema.
2. Navega al directorio del proyecto:
    ```bash
    cd BasicCalculator
    ```
3. Ejecuta el archivo de pruebas con el comando:
    ```bash
    python -m unittest test_calculator.py
    ```

## Estilo de Código
Para mantener la calidad del código, se está utilizando **Flake8** para verificar el estilo y las normas de codificación.

```bash
#!/bin/sh
FILES=$(git diff --cached --name-only --diff-filter=ACM)
echo "Ejecutando linting..."
for FILE in $FILES; do
    if [[ "$FILE" =~ \.py$ ]]; then  # Cambie a .py para archivos de Python
        flake8 "$FILE"  # Cambie a flake8 que es una librería de python
        if [ $? -ne 0 ]; then
            echo "Errores de linting encontrados en el archivo $FILE. Commit abortado."
            exit 1
        fi
    fi
done
exit 0
```
# CI QA Workflow - BasicTkinterCalculator
Este repositorio implementa un flujo de trabajo de integración continua (CI) para verificar la calidad del código mediante la ejecución de pruebas unitarias en cada pull request hacia la rama qa. El objetivo es asegurar que el código funciona correctamente antes de ser integrado en el entorno de calidad (QA).

# CI QA Workflow
## Descripción
El flujo de trabajo se ejecuta automáticamente cada vez que se crea o actualiza un pull request hacia la rama qa. Durante la ejecución, el sistema realiza las siguientes tareas:

1. Descarga el código del repositorio.
2. Configura el entorno de Python con la versión 3.8.
3. Instala y actualiza las dependencias necesarias.
4. Ejecuta las pruebas unitarias para verificar que el código es funcional.
5. Si las pruebas son exitosas, despliega la aplicación en el servidor de producción.

## Configuración del Flujo de Trabajo
El flujo de trabajo de integración continua (CI) se activa cuando se crea o actualiza un pull request hacia la rama qa. El proceso se ejecuta en un entorno de Ubuntu y consta de varios pasos: primero, se realiza la verificación del código fuente del repositorio; luego, se configura el entorno de Python con la versión 3.8. A continuación, se instalan las dependencias necesarias, y se ejecutan pruebas unitarias para verificar el correcto funcionamiento de la aplicación. Si alguna de las pruebas falla, se genera un mensaje indicando que las pruebas no pasaron, lo que permite a los desarrolladores identificar y solucionar problemas antes de fusionar los cambios en la rama principal.

## Implementación del CD con Vercel
Para la fase de Continuous Deployment (CD) del proyecto, la calculadora web se desplegará utilizando Vercel, una plataforma que facilita el despliegue de aplicaciones web. Vercel permite realizar despliegues automáticos cada vez que se realiza un push a la rama principal del repositorio. Esto asegura que cualquier cambio en el código se refleje inmediatamente en el entorno de producción, garantizando así que los usuarios siempre tengan acceso a la versión más reciente de la aplicación.


## Implementación del CD del Ejecutable
Para la fase de Continuous Deployment (CD) del proyecto, se creó un ejecutable. El ejecutable fue generado utilizando la herramienta PyInstaller, que convierte los archivos .py en un ejecutable independiente que contiene todo lo necesario para ejecutar el programa. Esto elimina la necesidad de un intérprete de Python o dependencias externas en el sistema del usuario final.

### Pasos para Generar el Ejecutable
1. Instalación de PyInstaller: Antes de crear el ejecutable, se debe instalar PyInstaller en el entorno de desarrollo. Para ello, se utiliza el siguiente comando:
    ```bash
    pip install pyinstaller
    ```
2. Generación del Ejecutable: Una vez instalado PyInstaller, se procede a crear el ejecutable a partir del archivo principal de la calculadora (calculadora.py). El comando es el siguiente:
    ```bash
    pyinstaller --onefile TkinterCalculadora.py
    ```

## Detalles Técnicos
- **Plataforma**: El flujo de trabajo se ejecuta en la versión más reciente de Ubuntu.
- **Entorno Python**: Se utiliza Python 3.8 para la ejecución del código.
- **Dependencias**: El flujo de trabajo asegura que pip está actualizado antes de ejecutar las pruebas.
- **Pruebas Unitarias**: Se ejecutan utilizando el módulo unittest en Python, evaluando el archivo test_calculator.py.
- **Manejo de Fallos**: Si las pruebas fallan, el proceso de CI se detendrá y subirá los resultados de las fallas.

## Cómo Funciona
Este flujo de trabajo es esencial para mantener la calidad del código en el proyecto. Automatiza el proceso de verificación antes de que cualquier cambio sea integrado en la rama qa, lo que ayuda a reducir el riesgo de introducir errores en el entorno de pruebas.

## Contribuidores
- Rayfel Ogando (#1107535) - [Rayfel2](https://github.com/Rayfel2)
- Eladio Tavarez (#1108874) - [Eventr077](https://github.com/Eventr077)
- Diego Rodriguez (#1105880) - [D1egoSebastian](https://github.com/D1egoSebastian)
- Axel Felix (#1106662) - [Notengonombredisponible](https://github.com/Notengonombredisponible)
- Andres Taveras (#1107975) - [FandresT101](https://github.com/FandresT101)
- Angel Soriano (#1107555) - [LoyaKnight](https://github.com/LoyaKnight)
