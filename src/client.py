import os
import grpc
import random

from schema.calculator_pb2_grpc import CalculatorServiceStub
from schema.calculator_pb2 import CalculatorRequest

class CalculatorClient:
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = CalculatorServiceStub(self.channel)

    def add_numbers(self, number1, number2):
        request = CalculatorRequest(number1=number1, number2=number2)
        return self.stub.AddNumbers(request)

    def subtract_numbers(self, number1, number2):
        request = CalculatorRequest(number1=number1, number2=number2)
        return self.stub.SubtractNumbers(request)

    def multiply_numbers(self, number1, number2):
        request = CalculatorRequest(number1=number1, number2=number2)
        return self.stub.MultiplyNumbers(request)

    def divide_numbers(self, number1, number2):
        request = CalculatorRequest(number1=number1, number2=number2)
        return self.stub.DivideNumbers(request)

def run():
    client = CalculatorClient(host="localhost", port=50051)

    # Generate two random float numbers between 5.0 and 25.0
    number1 = random.uniform(5.0, 25.0)  # Generates a random float
    number2 = random.uniform(5.0, 25.0)  # Generates a random float

    # Perform addition
    add_response = client.add_numbers(number1, number2)
    print(f"The sum of {number1} and {number2} is {add_response.result}")

    # Perform subtraction
    subtract_response = client.subtract_numbers(number1, number2)
    print(f"The difference when subtracting {number2} from {number1} is {subtract_response.result}")

    # Perform multiplication
    multiply_response = client.multiply_numbers(number1, number2)
    print(f"The product of {number1} and {number2} is {multiply_response.result}")

    # Perform division
    if number2 != 0.0:  # Ensure number2 is not zero
        divide_response = client.divide_numbers(number1, number2)
        print(f"The quotient of {number1} divided by {number2} is {divide_response.result}")
    else:
        print(f"Cannot divide {number1} by zero.")

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    run()
