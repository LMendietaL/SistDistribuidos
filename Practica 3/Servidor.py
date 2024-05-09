import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    try:
        operator, num1, num2 = request.split(",")
        num1 = float(num1)
        num2 = float(num2)
        if operator == "suma":
            result = num1 + num2
        elif operator == "resta":
            result = num1 - num2
        elif operator == "multiplicacion":
            result = num1 * num2
        elif operator == "division":
            result = num1 / num2
        else:
            result = "Operacion Invalida"
    except ValueError:
        result = "Invalid input"
    client_socket.send(str(result).encode())
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen(5)
    print("[*] Escuchando en 127.0.0.1:5555")

    while True:
        client, addr = server.accept()
        print(f"[*] Conexion aceptada de {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()