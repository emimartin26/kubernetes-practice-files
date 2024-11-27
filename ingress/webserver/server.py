import socket

def handle_request(client_socket):
    # Obtener el nombre del host
    host_name = socket.gethostname()

    # Recibir la solicitud del cliente
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Solicitud recibida:\n{request}")

    # Preparar la respuesta HTTP con el nombre del host
    http_response = f"""HTTP/1.1 200 OK
Content-Type: text/html

<html>
    <head><title>Mi servidor web</title></head>
    <body>
        <h1>¡Hola, Mundo!</h1>
        <p>Este es un servidor web básico en Python sin usar librerías externas.</p>
        <p>El nombre del host es: <strong>{host_name}</strong></p>
    </body>
</html>
"""
    # Enviar la respuesta HTTP al cliente
    client_socket.sendall(http_response.encode('utf-8'))
    client_socket.close()

def run_server(host='0.0.0.0', port=8080):
    # Crear un socket de tipo TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincular el socket al host y puerto especificados
    server_socket.bind((host, port))

    # Escuchar solicitudes entrantes (max 5 conexiones simultáneas)
    server_socket.listen(5)
    print(f"Servidor escuchando en {host}:{port}...")

    while True:
        # Aceptar una conexión entrante
        client_socket, client_address = server_socket.accept()
        print(f"Conexión desde {client_address}")

        # Manejar la solicitud del cliente
        handle_request(client_socket)

if __name__ == "__main__":
    run_server()