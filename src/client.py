import os
from calculator_client import CalculatorClient
from calculator_sim import CalculatorSimulator


def run():
    client = CalculatorClient(host="localhost", port=50051)
    calc_simulator = CalculatorSimulator(client)
    calc_simulator.simulate_calculator()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    run()
