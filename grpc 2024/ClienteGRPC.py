import grpc

import counter_pb2
import counter_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = counter_pb2_grpc.LetterCounterStub(channel)
    sentence = input("Por favor, ingresa una oración: ")
    response = stub.CountLetters(counter_pb2.Text(content=sentence))
    print("Número de letras en la oración:", response.count)

if __name__ == '__main__':
    run()