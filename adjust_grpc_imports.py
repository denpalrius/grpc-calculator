#!/usr/bin/env python3

import os
import re

def adjust_imports(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Adjust import statements for your directory structure
    content = re.sub(
        r'import calculator_pb2 as calculator__pb2',
        'import schema.calculator_pb2 as calculator__pb2',
        content
    )
    content = re.sub(
        r'import calculator_pb2_grpc as calculator__pb2_grpc',
        'import schema.calculator_pb2_grpc as calculator__pb2_grpc',
        content
    )

    with open(file_path, 'w') as file:
        file.write(content)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('_pb2_grpc.py'):
                file_path = os.path.join(root, file)
                adjust_imports(file_path)
                print(f"Adjusted imports in {file_path}")

if __name__ == "__main__":
    proto_dir = "./schema"
    process_directory(proto_dir)
    print("Import adjustments completed.")
