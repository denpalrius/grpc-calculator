# gRPC Calculator

This project is a gRPC-based calculator service that performs basic arithmetic operations. The service is implemented in `Python` and uses the gRPC framework for communication.

## Project Structure

- **calculator.proto**: Protocol Buffers definition file that describes the gRPC service and messages.
- **calculator_pb2.py**: Generated Python code from the `calculator.proto` file (contains message classes).
- **calculator_pb2_grpc.py**: Generated Python code from the `calculator.proto` file (contains service classes).
- **server.py**: Implementation of the gRPC server that provides the calculator service.
- **client.py**: Implementation of a gRPC client that interacts with the calculator service.

## Getting Started

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/denpalrius/grpc-calculator
    cd grpc-calculator
    ```

3. Alternatively, install the required packages using the `requirements.txt` file:
    ```sh
    pip install -r requirements.txt
    ```

### Generate gRPC Code Using Bash Script

You can also use the provided `generate_proto.sh` script to regenerate the gRPC code:
```sh
./proto_gen.sh
```

### Running the Server

Start the gRPC server:
```sh
python server.py
```

### Running the Client

In another terminal, run the gRPC client:
```sh
python client.py
```

## Acknowledgements

- [gRPC](https://grpc.io/)
- [Protocol Buffers](https://developers.google.com/protocol-buffers)
