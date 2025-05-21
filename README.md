# BX Operator - Advanced Matrix Operations Suite

## Overview

BX Operator is a command-line interface (CLI) tool designed for performing advanced operations on sparse matrices. It supports loading matrices from files, performing various matrix operations, and displaying results in a user-friendly format.


## Features

- **Loading and Displaying Matrices**
  - Load matrices from files
  - Display matrices in a readable format

- **Matrix Operations**
  - Addition, Subtraction, Multiplication
  - Transposition
  - Conversion to Compressed Sparse Row (CSR) format

- **Error Handling**
  - Detailed error messages for file format issues and dimension mismatches

## Installation

1. Clone the repository:
    ```sh
    https://github.com/ulrichr7/Sparse-Matrix.git
    ```
2. Navigate to the project directory:
    ```sh
    cd BXOperator
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

!Installation

## Usage

1. Start the CLI:
    ```sh
    python main.py
    ```
2. Use the following commands to interact with the tool:
    - `load <file_path1> <file_path2>`: Load two matrices from specified files
    - `opp + <file_output.txt>`: Perform matrix addition
    - `opp - <file_output.txt>`: Perform matrix subtraction
    - `opp * <file_output.txt>`: Perform matrix multiplication
    - `help`: Display the help menu
    - `exit`: Exit the application


## File Format Requirements

- Input files should contain space-separated numbers
- Each line represents a row in the matrix
re- All rows must have the same number of columns
- Example format:
    ```
    rows=10
    cols=10
    (1 0 0)
    (0 1 0)
    (0 0 1)
    ```

## Error Handling

- Success indicators show when operations complete
- Error messages explain why operations fail
- Loading errors indicate file format issues
- Dimension mismatch errors show specific requirements

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
