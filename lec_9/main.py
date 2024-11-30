
class Matrix:
    def __init__(self, rows, cols, elements=None):
        self.rows = rows
        self.cols = cols
        if elements:
            if len(elements) != rows or any(len(row) != cols for row in elements):
                raise ValueError("Invalid dimensions for the given elements.")
            self.matrix = elements
        else:
            self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(self.rows, self.cols, result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        result = [
            [self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(self.rows, self.cols, result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")
        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(self.rows, other.cols, result)



matrix_a = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
print("Matrix A:")
print(matrix_a)

matrix_b = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])
print("\nMatrix B:")
print(matrix_b)

matrix_c = matrix_a + matrix_b
print("\nMatrix A + Matrix B:")
print(matrix_c)

matrix_d = matrix_a - matrix_b
print("\nMatrix A - Matrix B:")
print(matrix_d)

matrix_e = Matrix(3, 2, [[1, 4], [2, 5], [3, 6]])
matrix_f = matrix_a * matrix_e
print("\nMatrix A * Matrix E:")
print(matrix_f)
