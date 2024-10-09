import grpc
from schema import calculator_pb2_grpc, calculator_pb2


class CalculatorClient:
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = calculator_pb2_grpc.CalculatorServiceStub(self.channel)

    def add_numbers(self, number1, number2):
        request = calculator_pb2.CalculatorRequest(number1=number1, number2=number2)
        return self.stub.AddNumbers(request)

    def subtract_numbers(self, number1, number2):
        request = calculator_pb2.CalculatorRequest(number1=number1, number2=number2)
        return self.stub.SubtractNumbers(request)

    def multiply_numbers(self, number1, number2):
        request = calculator_pb2.CalculatorRequest(number1=number1, number2=number2)
        return self.stub.MultiplyNumbers(request)

    def divide_numbers(self, number1, number2):
        request = calculator_pb2.CalculatorRequest(number1=number1, number2=number2)
        return self.stub.DivideNumbers(request)

        
