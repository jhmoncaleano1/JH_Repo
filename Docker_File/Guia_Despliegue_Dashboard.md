# Guía de Despliegue: Dashboard de Cartera en Docker

Esta guía explica cómo construir y ejecutar el dashboard desarrollado con Streamlit dentro de un contenedor Docker.

---

## 📁 Archivos Incluidos

- `Dockerfile`: Define el entorno del contenedor.
- `requirements.txt`: Lista de dependencias.
- `dashboard_cartera.py`: Código del dashboard.
- `Cartera.xlsx`: Archivo de datos.

---

## 🐳 Requisitos Previos

- Tener instalado **Docker** en tu equipo.
  - Puedes descargarlo desde: https://www.docker.com/products/docker-desktop/

---

## ⚙️ Pasos para Construir y Ejecutar

### 1. Extraer los archivos

Descomprime `dashboard_docker_package.zip` en una carpeta local.

### 2. Abrir una terminal en esa carpeta

Usa tu terminal o línea de comandos y navega a la carpeta con los archivos.

### 3. Construir la imagen de Docker

```bash
docker build -t dashboard-cartera .
