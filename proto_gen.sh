#!/bin/bash

# Define the proto files and output directory
PROTO_FILE="calculator.proto"
OUTPUT_DIR="./schema"

# Remove the output directory if it exists
rm -rf "$OUTPUT_DIR"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Compile proto file
python -m grpc_tools.protoc \
    --proto_path=. \
    --python_out="$OUTPUT_DIR" \
    --grpc_python_out="$OUTPUT_DIR" \
    $PROTO_FILE

echo "Compilation of proto file completed successfully. Output is in $OUTPUT_DIR/$PROTO_FILE"