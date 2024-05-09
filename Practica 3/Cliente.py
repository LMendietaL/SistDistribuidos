import socket

def send_request(operation, num1, num2):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))
    client.send(f"{operation},{num1},{num2}".encode())
    response = client.recv(1024).decode()
    print(f"Resultado: {response}")
    client.close()

if __name__ == "__main__":
    operation = input("ingrese la operacion (suma/resta/multiplicacion/division): ")
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    send_request(operation, num1, num2)