#!/usr/bin/env python3
class SparseMatrix:
    def __init__(self, data, rows=None, columns=None):
        self.data = data
        self.rows = rows if rows is not None else len(data)
        self.columns = columns if columns is not None else max(len(row) for row in data)

    def transpose(self):
        transposed_matrix = []
        for i in range(self.columns):
            transposed_row = []
            for j in range(self.rows):
                if j < len(self.data) and i < len(self.data[j]):
                    transposed_row.append(self.data[j][i])
                else:
                    transposed_row.append(0)
            transposed_matrix.append(transposed_row)
        return SparseMatrix(transposed_matrix, self.columns, self.rows)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(f"rows={self.rows}\n")
            f.write(f"cols={self.columns}\n")
            for row in self.data:
                # Remove trailing zeros
                while row and row[-1] == 0:
                    row.pop()
                if row:
                    f.write(f"({', '.join(map(str, row))})\n")
                else:
                    f.write("\n")
    
    def to_csr(self):
        csr_matrix = {'data': [], 'indices': [], 'indptr': [0]}
        for row in self.data:
            for col, value in enumerate(row):
                if value != 0:
                    csr_matrix['data'].append(value)
                    csr_matrix['indices'].append(col)
            csr_matrix['indptr'].append(len(csr_matrix['data']))
        # Ensure indptr has the correct length
        while len(csr_matrix['indptr']) <= self.columns:
            csr_matrix['indptr'].append(len(csr_matrix['data']))
        return csr_matrix


class Operations:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def addition(self):
        csr_matrix1 = self.matrix1.to_csr()
        csr_matrix2 = self.matrix2.to_csr()
    
        result = [[0] * self.matrix2.columns for _ in range(self.matrix1.rows)]
    
        for i in range(self.matrix1.rows):
            row_start1 = csr_matrix1['indptr'][i]
            row_end1 = csr_matrix1['indptr'][i + 1]
            row_start2 = csr_matrix2['indptr'][i]
            row_end2 = csr_matrix2['indptr'][i + 1]
    
            for j in range(row_start1, row_end1):
                col = csr_matrix1['indices'][j]
                val1 = csr_matrix1['data'][j]
                result[i][col] += val1
    
            for j in range(row_start2, row_end2):
                col = csr_matrix2['indices'][j]
                val2 = csr_matrix2['data'][j]
                result[i][col] += val2
    
        return SparseMatrix(result, self.matrix1.rows, self.matrix2.columns)
    
    def subtraction(self):
        csr_matrix1 = self.matrix1.to_csr()
        csr_matrix2 = self.matrix2.to_csr()
    
        result = [[0] * self.matrix2.columns for _ in range(self.matrix1.rows)]
    
        for i in range(self.matrix1.rows):
            row_start1 = csr_matrix1['indptr'][i]
            row_end1 = csr_matrix1['indptr'][i + 1]
            row_start2 = csr_matrix2['indptr'][i]
            row_end2 = csr_matrix2['indptr'][i + 1]
    
            for j in range(row_start1, row_end1):
                col = csr_matrix1['indices'][j]
                val1 = csr_matrix1['data'][j]
                result[i][col] += val1
    
            for j in range(row_start2, row_end2):
                col = csr_matrix2['indices'][j]
                val2 = csr_matrix2['data'][j]
                result[i][col] -= val2
    
        return SparseMatrix(result, self.matrix1.rows, self.matrix2.columns)

    
    def multiplication(self):
        csr_matrix1 = self.matrix1.to_csr()
        csr_matrix2 = self.matrix2.to_csr()
    
    
        result = [[0] * self.matrix2.columns for _ in range(self.matrix1.rows)]
    
        for i in range(self.matrix1.rows):
            row_start = csr_matrix1['indptr'][i]
            row_end = csr_matrix1['indptr'][i + 1]
            for j in range(row_start, row_end):
                col = csr_matrix1['indices'][j]
                val1 = csr_matrix1['data'][j]
                if col < len(csr_matrix2['indptr']) - 1:
                    col_start = csr_matrix2['indptr'][col]
                    col_end = csr_matrix2['indptr'][col + 1]
                    for k in range(col_start, col_end):
                        if k < len(csr_matrix2['indices']) and csr_matrix2['indices'][k] < self.matrix2.columns:
                            result[i][csr_matrix2['indices'][k]] += val1 * csr_matrix2['data'][k]
                        else:
                            print(f"      Skipping k={k} as it is out of range for csr_matrix2['indices']")
                else:
                    print(f"  Skipping col={col} as it is out of range for csr_matrix2['indptr']")
    
        return SparseMatrix(result, self.matrix1.rows, self.matrix2.columns)