# Task List

Aplicación web sencilla hecha con Django para gestionar una lista de tareas.

## Descripción

Este proyecto incluye:

- Modelo `Task` con título, fecha de creación y fecha de actualización.
- Vista principal que muestra la lista de tareas.
- Configuración básica para ejecutar el proyecto con SQLite.

## Requisitos

- Python 3.12+
- pip
- virtualenv (opcional, pero recomendado)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <url-del-repositorio>
   cd task-list
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplica las migraciones:

   ```bash
   python manage.py migrate
   ```

5. Inicia el servidor:

   ```bash
   python manage.py runserver
   ```

6. Abre la aplicación en tu navegador:

   ```text
   http://127.0.0.1:8000/
   ```

## Estructura del proyecto

```text
.
├── db.sqlite3
├── manage.py
├── requirements.txt
├── django_base/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── tasks/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── task-list.html
└── README.md
```

## Modelo principal

El modelo `Task` se define en `tasks/models.py` y contiene:

- `title`: título de la tarea
- `created_at`: fecha de creación
- `updated_at`: fecha de última actualización

## Uso

La página principal muestra la lista de tareas. Puedes personalizar la plantilla de la vista en `templates/task-list.html`.

## Comandos útiles

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Licencia

Este proyecto se proporciona tal cual para fines de aprendizaje y desarrollo.
