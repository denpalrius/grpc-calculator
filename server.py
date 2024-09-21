from concurrent import futures
import grpc
from square_pb2 import Result
import square_pb2_grpc
import math


class SquareService(square_pb2_grpc.SquareServiceServicer):
    def Square(self, request, context):
        square = math.pow(request.value, 2)
        return Result(value=square)
    

def serve():
    print("Starting server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    square_pb2_grpc.add_SquareServiceServicer_to_server(SquareService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    print("Server started at 50051.")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
