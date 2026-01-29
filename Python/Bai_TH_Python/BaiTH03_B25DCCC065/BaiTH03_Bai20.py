matrix = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]
def sum_main_diagonal(mat):
    total = 0
    for i in range(len(mat)):
        total += mat[i][i]
    return total
def sum_secondary_diagonal(mat):
    total = 0
    n = len(mat)
    for i in range(n):
        total += mat[i][n - 1 - i]
    return total
def matrix_to_tuple_of_tuples(mat):
    return tuple(tuple(row) for row in mat)
main_diagonal_sum = sum_main_diagonal(matrix)
secondary_diagonal_sum = sum_secondary_diagonal(matrix)
tuple_of_tuples = matrix_to_tuple_of_tuples(matrix)
print("Tổng các số ở đường chéo chính:", main_diagonal_sum)
print("Tổng các số ở đường chéo phụ:", secondary_diagonal_sum)
print("Ma trận dưới dạng tuple của tuple:", tuple_of_tuples)