
class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        print(f"Enter the elements of the {n}x{m}:")
        self.matrix = []
        for i in range(n):
            row = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row) != m:
                raise ValueError(f"Each row must contain exactly {m} elements.")
            self.matrix.append(row)

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))

    def calculate_mean(self):
        total_elements = self.n * self.m
        total_sum = sum(sum(row) for row in self.matrix)
        return total_sum / total_elements

    def row_sum(self, row):
        if 0 <= row < self.n:
            return sum(self.matrix[row])
        else:
            raise IndexError("Row index out of range.")

    def column_average(self, col):
        if 0 <= col < self.m:
            column_sum = sum(self.matrix[i][col] for i in range(self.n))
            return column_sum / self.n
        else:
            raise IndexError("Column index out of range.")

    def print_submatrix(self, col1, col2, row1, row2):
        if not (0 <= col1 <= col2 < self.m and 0 <= row1 <= row2 < self.n):
            raise IndexError("error.")
        for i in range(row1, row2 + 1):
            print(" ".join(map(str, self.matrix[i][col1:col2 + 1])))



n, m = 4, 5  
matrix = Matrix(n, m)  

print("\nMatrix:")
matrix.print_matrix()

print("\nMean of the matrix:", matrix.calculate_mean())

row = 1
print(f"\nSum of row {row}:", matrix.row_sum(row))

col = 2
print(f"\nAverage of column {col}:", matrix.column_average(col))

print("\nSubmatrix [col1=1, col2=3, row1=0, row2=1]:")
matrix.print_submatrix(1, 3, 0, 1)
