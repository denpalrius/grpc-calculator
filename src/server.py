from concurrent import futures
import os
import grpc
from calculator_service import CalculatorService
from schema import calculator_pb2_grpc


def serve():
    print("CalculatorService: Starting...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServiceServicer_to_server(CalculatorService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()

    print("CalculatorService: Server started at 50051.")
    server.wait_for_termination()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    serve()
