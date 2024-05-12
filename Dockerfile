# Usar una imagen base de Python oficial
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias del sistema para PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requisitos y instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto en el que Django se ejecutará
EXPOSE 8000

# Comando para ejecutar la aplicación usando Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gestion_residuos.wsgi:application"]


# # Usar imagen base de Python
# FROM python:3.11-slim

# # Establecer directorio de trabajo
# WORKDIR /app

# # Instalar dependencias necesarias para el proyecto
# # RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*
# # Instalar las dependencias requeridas para psycopg2
# RUN apt-get update && apt-get install -y \
#     gcc \
#     python3-dev \
#     libpq-dev && \
#     rm -rf /var/lib/apt/lists/*

# # Actualizar pip
# RUN pip install --upgrade pip

# # Instalar dependencias de Python
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # Copiar el código fuente del proyecto
# COPY . .

# # Compilar archivos estáticos
# RUN python manage.py collectstatic --noinput

# # Exponer puerto y definir comando por defecto para ejecutar la aplicación
# EXPOSE 8000
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "gestion_residuos.wsgi:application"]
