#!/bin/bash

# Define the proto file and output directory
PROTO_FILE="greeting.proto"
OUTPUT_DIR="lib"

# Clean up the schema directory
rm -rf $OUTPUT_DIR

# Create the output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Compile the proto file using betterproto
python -m grpc_tools.protoc \
    -I . \
    --python_betterproto_out=$OUTPUT_DIR \
    ./protos/$PROTO_FILE

echo "Compilation of $PROTO_FILE completed. Output is in $OUTPUT_DIR"
