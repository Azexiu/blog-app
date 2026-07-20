# 🚀 Deploy de Django en Render (URL pública)

Este documento explica el paso a paso para desplegar una aplicación Django en Render y obtener una URL pública accesible desde cualquier navegador.

---

## 🧱 1. Subir el proyecto a GitHub

Inicializar repositorio:

```bash
git init
git add .
git commit -m "deploy inicial"
git branch -M main
git remote add origin <URL_DEL_REPO>
git push -u origin main
```

## 📦 2. Instalar dependencias necesarias
```
pip install gunicorn whitenoise
pip freeze > requirements.txt
```

## ⚙️ 3. Configuración en settings.py
```
ALLOWED_HOSTS = ["*"]

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
```
Agregar en MIDDLEWARE en settings.py:
```
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    ...
]
```

## 📄 4. Crear Procfile (opcional en Render, pero recomendado)

En la raíz del proyecto:
```
web: gunicorn config.wsgi:application
```
Reemplazar config por el nombre real de tu proyecto Django.

## 🌐 5. Crear cuenta en Render

1. Ir a https://render.com
2. Iniciar sesión con GitHub
3. Seleccionar New Web Service

## 🔗 6. Conectar repositorio

1. Elegir el repositorio del proyecto
2. Seleccionar la rama main

## ⚙️ 7. Configuración del servicio

### Completar los campos:
Runtime
```
Python
```
Build Command
```
pip install -r requirements.txt
```
Start Command
```
gunicorn config.wsgi:application
```
## 🌍 8. Variables de entorno

```
PYTHON_VERSION=3.11
```

## 🚀 9. Deploy

Render ejecutará automáticamente:

- instalación de dependencias
- build del proyecto
- despliegue del servidor

## 🧪 10. Migraciones (si es necesario)

En local :
```
python manage.py migrate
```
## 🎯 11. URL final
```
https://tu-proyecto.onrender.com
```