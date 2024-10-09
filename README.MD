# gRPC Calculator Service

This is a gRPC service for basic arithmetic operations (addition, subtraction, multiplication, division) using Protocol Buffers for efficient communication between server and client.

## Features

- **Addition, Subtraction, Multiplication, Division**: Perform arithmetic operations on two float numbers.
- **gRPC Server**: Serves calculation requests.
- **gRPC Client**: Sends simulated calculation requests and receives responses.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/denpalrius/grpc-calculator
    cd grpc-calculator
    ```

2. Create and activate a new conda environment:

    ```bash
    # Use your own Python version
    conda create --name rpc_env python=3.12 -y
    conda activate rpc_env
    ```

3. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Generate gRPC code:

    ```bash
    ./proto_gen.sh
    ```

    This will generate the gRPC python code in the `./schema` directory

## Running

1. Start the gRPC server:

    ```bash
    PYTHONPATH=$PYTHONPATH:. python src/server.py
    ```

2. In another terminal, run the gRPC client:

    ```bash
    PYTHONPATH=$PYTHONPATH:. python src/client.py
    ```

## Project Structure

- **client.py**: gRPC client to perform operations.
- **server.py**: gRPC server to handle requests.
- **calculator_service.py**: Implements the calculator service logic.
- **calculator.proto**: Protocol Buffers definition.
- **proto_gen.sh**: Script to generate gRPC Python code from `.proto` files.

## Example Output

```bash
The sum of 10.5 and 7.3 is 17.8
The difference when subtracting 7.3 from 10.5 is 3.2
The product of 10.5 and 7.3 is 76.65
The quotient of 10.5 divided by 7.3 is 1.44
```

## Notes

- The server listens on `localhost:50051`.
- Ensure both server and client are using the same port.
