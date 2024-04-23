import grpc
from concurrent import futures
import time

import counter_pb2
import counter_pb2_grpc

class LetterCounter(counter_pb2_grpc.LetterCounterServicer):
    def CountLetters(self, request, context):
        letter_count = len(request.content.replace(" ", "")) # Eliminar espacios y contar letras
        return counter_pb2.Count(count=letter_count)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    counter_pb2_grpc.add_LetterCounterServicer_to_server(LetterCounter(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started. Listening on port 50051.")
    try:
        while True:
            time.sleep(86400) # 1 día en segundos
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()