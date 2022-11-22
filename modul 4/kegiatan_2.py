def transpose(function):
    def wrapper(*args, **kwargs):
        matrix = function(*args, **kwargs)
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    return wrapper


@transpose
def Tmatrix(m):
    Tm = [[m[0], m[1]],
          [m[2], m[3]]]
    return Tm


def penjumlahanMatrix(function1, function2):
    Yt = function1
    Z = function2
    hasilJumlah = [[0, 0],
                   [0, 0]]

    # iterate through rows
    for i in range(len(Yt)):
        # iterate through columns
        for j in range(len(Yt[0])):
            hasilJumlah[i][j] = Yt[i][j] + Z[i][j]

    return hasilJumlah


def perkalianMatrix(function):
    def kali(matrix):
        At = Tmatrix(function)
        X = [[matrix[0], matrix[1]],
             [matrix[2], matrix[3]]]
        AtX = [[0, 0],
               [0, 0]]

        # iterate through rows of X
        for i in range(len(At)):
            # iterate through columns of Y
            for j in range(len(X[0])):
                # iterate through rows of Y
                for k in range(len(X)):
                    AtX[i][j] += At[i][k] * X[k][j]
        return AtX

    return kali


def resultMatrix(X, Y, A):
    Z = perkalianMatrix(A)(X)
    result = penjumlahanMatrix(Tmatrix(Y), Z)
    return result


# Test case 1:

# Input:
matrixX = [4, 7, 8, 5]
matrixY = [3, 2, 7, 5]
matrixA = [9, 7, 6, 2]

# Output: [87, 46, 100, 64]
x = resultMatrix(matrixX, matrixY, matrixA)
print("Test Case 1:\n")
print(matrixX)
print(matrixY)
print(matrixA)

print("\nOutput: ")
print([x[i][j] for j in range(len(x[0])) for i in range(len(x))])