#!/bin/bash

# Define the proto file and output directory
PROTO_FILE="calc.proto"
OUTPUT_DIR="./"

# Create the output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Compile the proto file
python -m grpc_tools.protoc \
 --proto_path=. \
 --python_out=$OUTPUT_DIR \
 --grpc_python_out=$OUTPUT_DIR \
 $PROTO_FILE

echo "Compilation of $PROTO_FILE completed. Output is in $OUTPUT_DIR"