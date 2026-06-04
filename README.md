<p align="center">
  <img src="static/logo.svg" width="120" alt="basic-tkinter-calculator logo">
</p>

<h1 align="center">basic-tkinter-calculator</h1>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python Version"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>

<p align="center">
  Calculadora dual: una aplicación de escritorio desarrollada con <strong>Tkinter</strong> y una calculadora web construida con <strong>Flask</strong>. Ambas permiten realizar operaciones matemáticas básicas de forma sencilla.
</p>

## Características

- **Calculadora de Escritorio (Tkinter):** Interfaz gráfica nativa, liviana y sin dependencias externas para ejecutar (una vez empaquetada).
- **Calculadora Web (Flask):** Accesible desde cualquier navegador con una interfaz moderna y responsiva.
- **Lógica Segura:** Evaluación de expresiones matemáticas mediante parser seguro, sin uso de `eval()`.
- **Tests Automatizados:** Cobertura de pruebas unitarias para la lógica de negocio y la aplicación web.

## Screenshots

| Escritorio | Web |
|---|---|
| ![Desktop](static/screenshots/desktop.png) | ![Web](static/screenshots/web.png) |

## Tecnologías

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (GUI de escritorio)
- [Flask](https://flask.palletsprojects.com/) (Microframework web)
- [PyInstaller](https://pyinstaller.org/) (Empaquetado del ejecutable)

## Instalación y Uso

### Prerrequisitos

- Python 3.10 o superior.
- pip (gestor de paquetes de Python).

### Clonar el repositorio

```bash
git clone https://github.com/Rayfel2/BasicTkinterCalculator.git
cd BasicTkinterCalculator
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Calculadora de Escritorio

```bash
python TkinterCalculadora.py
```

Para generar el ejecutable standalone:

```bash
pyinstaller --onefile --windowed TkinterCalculadora.py
# El ejecutable se encuentra en dist/TkinterCalculadora.exe
```

### Calculadora Web

```bash
python app.py
```

Abre tu navegador en `http://127.0.0.1:5000`.

> **Despliegue en producción:** La aplicación web está configurada para desplegarse directamente en [Vercel](https://vercel.com/). El archivo `vercel.json` ya está preparado.

## Despliegue

### Web (Vercel)

1. Ve a [vercel.com](https://vercel.com) e inicia sesión.
2. Clic en **Add New... > Project**.
3. Importa tu repositorio `BasicTkinterCalculator` desde GitHub.
4. Vercel detectará automáticamente la configuración de `vercel.json`.
5. Clic en **Deploy**. Listo.

Cada push a `main` actualizará automáticamente la web.

### Ejecutable de Escritorio

El workflow `ci.yml` genera automáticamente un ejecutable `.exe` para Windows usando PyInstaller y lo publica como artifact en cada push a `main`.

## Tests

Ejecuta el conjunto de pruebas unitarias con:

```bash
python -m unittest test_calculator.py
```

Las pruebas validan:
- La lógica aritmética de ambas calculadoras.
- El manejo de errores (división por cero, sintaxis inválida).
- Las rutas y respuestas HTTP de la aplicación Flask.

## Contribuidores

- Rayfel Ogando ([@Rayfel2](https://github.com/Rayfel2))
- Eladio Tavarez ([@Eventr077](https://github.com/Eventr077))
- Diego Rodriguez ([@D1egoSebastian](https://github.com/D1egoSebastian))
- Axel Felix ([@Notengonombredisponible](https://github.com/Notengonombredisponible))
- Andres Taveras ([@FandresT101](https://github.com/FandresT101))
- Angel Soriano ([@LoyaKnight](https://github.com/LoyaKnight))

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).
