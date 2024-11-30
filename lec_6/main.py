import random
def random_matrix(rows, cols):
    return [[random.randint(1,10) for _ in range(cols)] for _ in range(rows)]

rows=4
cols=5
matrix=random_matrix(rows,cols)
for row in matrix:
    print(row)


def get_column_sum(matrix,col_index):
    sum_=0
    for row in matrix:
        if col_index<=rows: 
            sum_+=row[col_index]
    return sum_


col_index = 1
result = get_column_sum(matrix, col_index)
print(f"Sum of column {col_index}: {result}")

def get_row_average(matrix, row_index):
    if row_index < 0 or row_index >= len(matrix):
        raise IndexError("Row index out of range.")
    row = matrix[row_index]
    row_sum = sum(row)
    row_average = row_sum / len(row)

    return row_average

row_index = 1
result = get_row_average(matrix, row_index)
print(f"Average of row {row_index}: {result}")
