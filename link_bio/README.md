# Web de links de MoureDev

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![FastAPI](https://img.shields.io/badge/Reflex-0.3.6+-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://fastapi.tiangolo.com)

## Proyecto desarrollado con [Python](https://www.python.org/) y [Reflex](https://reflex.dev/) que representa un sitio web personal estilo "[link in bio](https://moure.dev/)"

## Requisitos

#### Crea un entorno virtual [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) en la raíz del proyecto
Mac/Linux: `python3 -m pip install virtualenv`

Windows: `py -m pip install --user virtualenv`

#### Activa el entorno virtual 
Mac/Linux: `source env/bin/activate`

Windows: `.\env\Scripts\activate`

Para desactivar el entorno virtual: `deactivate`

## Dependencias
*(Con el entorno virtual activo)*

`pip install reflex`

## Ejecución
`reflex run`

`reflex run --loglevel debug` *(modo debug)*

Acceder a [http://localhost:3000](http://localhost:3000) (frontend) y a [http://localhost:8000](http://localhost:8000) (backend)