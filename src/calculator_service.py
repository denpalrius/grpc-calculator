from schema import calculator_pb2, calculator_pb2_grpc

class CalculatorService(calculator_pb2_grpc.CalculatorServiceServicer):
    def calculate(self, request: calculator_pb2.CalculatorRequest, operation, operation_name):
        # Use float for calculations
        operations = {
            'add': lambda x, y: float(x) + float(y),
            'subtract': lambda x, y: float(x) - float(y),
            'multiply': lambda x, y: float(x) * float(y),
            'divide': lambda x, y: float(x) / float(y) if y != 0 else float('nan')  # Handle division by zero
        }

        result = operations[operation](request.number1, request.number2)
        print(f"CalculatorService: {operation_name} {request.number1} and {request.number2}. Returning {result}.")
        return calculator_pb2.CalculatorResponse(result=result)  # Ensure result is a float

    def AddNumbers(self, request: calculator_pb2.CalculatorRequest, context) -> calculator_pb2.CalculatorResponse:
        return self.calculate(request, 'add', 'Adding')

    def SubtractNumbers(self, request: calculator_pb2.CalculatorRequest, context) -> calculator_pb2.CalculatorResponse:
        return self.calculate(request, 'subtract', 'Subtracting')

    def MultiplyNumbers(self, request: calculator_pb2.CalculatorRequest, context) -> calculator_pb2.CalculatorResponse:
        return self.calculate(request, 'multiply', 'Multiplying')

    def DivideNumbers(self, request: calculator_pb2.CalculatorRequest, context) -> calculator_pb2.CalculatorResponse:
        return self.calculate(request, 'divide', 'Dividing')
