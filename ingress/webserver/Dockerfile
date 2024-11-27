# Usar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de servidor Python al contenedor
COPY server.py /app/server.py

# Exponer el puerto en el que el servidor web estará escuchando
EXPOSE 8080

# Comando para ejecutar el servidor cuando el contenedor arranque
CMD ["python", "server.py"]
