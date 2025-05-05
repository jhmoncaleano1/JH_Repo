# Usar una imagen base con Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios al contenedor
COPY requirements.txt .
COPY dashboard_cartera.py .
COPY Cartera.xlsx .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto usado por Streamlit
EXPOSE 8501

# Comando para ejecutar el dashboard
CMD ["streamlit", "run", "dashboard_cartera.py", "--server.port=8501", "--server.address=0.0.0.0"]
