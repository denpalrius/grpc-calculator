import os
import grpc
from square_pb2 import Number
from square_pb2_grpc import SquareServiceStub
import random


class CalculatorClient:
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = SquareServiceStub(self.channel)

    def get_square(self, number):
        request = Number(value=number)
        return self.stub.GetSquare(request)


def run():
    client = CalculatorClient(host="localhost", port=50051)

    # Generate a random number between 5 and 25
    number = random.randint(5, 25)

    response = client.get_square(number)
    print(f"The square of {number} is {response.value}")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    run()
