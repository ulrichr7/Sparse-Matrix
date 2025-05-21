#!/usr/bin/env python3
from classes import SparseMatrix

def parse_line(line):
    parts = line.strip('()').split(',')
    return [int(part.strip()) for part in parts]

def file_parser(file_path1, file_path2):

    def parse_file(file_path):
        rows, columns = None, None
        parsed_lines = []
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if 'row' in line or 'rows' in line:
                    rows = int(line.split('=')[-1].strip())
                elif 'col' in line or 'cols' in line:
                    columns = int(line.split('=')[-1].strip())
                elif line.startswith('('):
                    parsed_lines.append(parse_line(line))
        return parsed_lines, rows, columns

    parsed1, rows1, columns1 = parse_file(file_path1)
    parsed2, rows2, columns2 = parse_file(file_path2)

    matrix1 = SparseMatrix(parsed1, rows1, columns1)
    matrix2 = SparseMatrix(parsed2, rows2, columns2)

    return matrix1, matrix2

'''Operations Checker'''
def operaction_checker(Matrix1, Matrix2, operation):
    if operation == '+':
        if Matrix1.rows != Matrix2.rows or Matrix1.columns != Matrix2.columns:
            return False
        else:
            return True
    elif operation == '-':
        if Matrix1.rows != Matrix2.rows or Matrix1.columns != Matrix2.columns:
            return False
        else:
            return True
    elif operation == '*':
        if Matrix1.columns != Matrix2.rows:
            return False
        else:
            return True
    elif operation == 't':
        return True
    else:
        return False