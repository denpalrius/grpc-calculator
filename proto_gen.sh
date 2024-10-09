#!/bin/bash

# Define the proto files and output directory
PROTO_FILE="calculator.proto"
OUTPUT_DIR="./schema"

# Remove the output directory if it exists
rm -rf "$OUTPUT_DIR"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Create an empty __init__.py file to treat the schema folder as a package
touch "$OUTPUT_DIR/__init__.py"

# Generate Python code
echo -e "\nGenerating gRPC Python files..."
python -m grpc_tools.protoc \
    --python_out=${OUTPUT_DIR} \
    --pyi_out=${OUTPUT_DIR} \
    --grpc_python_out=${OUTPUT_DIR} \
    --proto_path="./" \
    ${PROTO_FILE}

# Run the Python script to adjust imports
echo -e "\nAdjusting imports in generated Python files..."
python3 ./adjust_grpc_imports.py

# Check if the Python script ran successfully
if [ $? -ne 0 ]; then
    echo -e "\nError: Import adjustment failed"
    exit 1
fi

echo "Compilation of proto file completed successfully. Output is in $OUTPUT_DIR"
