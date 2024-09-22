from concurrent import futures
import os
import grpc
from square_pb2 import Result
import square_pb2_grpc


class SquareService(square_pb2_grpc.SquareServiceServicer):
    def GetSquare(self, request, context):
        square =request.value ** 2
        print(f"SquareService: Received request for {request.value}. Returning {square}.")
        return Result(value=square)


def serve():
    print("SquareServer: Starting...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    square_pb2_grpc.add_SquareServiceServicer_to_server(SquareService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()

    print("SquareServer: Server started at 50051.")
    server.wait_for_termination()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    serve()
