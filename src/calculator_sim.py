import random


class CalculatorSimulator:
    def __init__(self, calculator_client):
        self.client = calculator_client

    def simulate_calculator(self):
        # Generate two random float numbers between 5.0 and 25.0
        number1 = float(round(random.uniform(5, 25)))
        number2 = float(round(random.uniform(5, 25)))

        # Perform addition
        add_response = self.client.add_numbers(number1, number2)
        print(f"The sum of {number1:.0f} and {number2:.0f} is {add_response.result:.0f}")

        # Perform subtraction
        subtract_response = self.client.subtract_numbers(number1, number2)
        print(f"The difference when subtracting {number2:.0f} from {number1:.0f} is {subtract_response.result:.0f}")

        # Perform multiplication
        multiply_response = self.client.multiply_numbers(number1, number2)
        print(f"The product of {number1:.0f} and {number2:.0f} is {multiply_response.result:.0f}")

        # Perform division
        if number2 != 0.0:  # Ensure number2 is not zero
            divide_response = self.client.divide_numbers(number1, number2)
            print(f"The quotient of {number1:.0f} divided by {number2:.0f} is {divide_response.result:.2f}")
        else:
            print(f"Cannot divide {number1:.0f} by zero.")
        
