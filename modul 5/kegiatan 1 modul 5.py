from functools import reduce


# fungsi transpose dengan inner function wrapper untuk menangkap inputan yang berupa
def transpose(function):
    def wrapper(*Args, **Kwargs):
        # fungsi untuk mentranspose matrix
        x = function(*Args, **Kwargs)
        result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
        return result

    return wrapper


# tambahkan dekorator untuk mentranspose matrix kofaktor
# 1 2 3    m[0][0] m[0][1] m[0][2]
# 4 5 6    m[1][0] m[1][1] m[1][2]
# 7 8 9    m[2][0] m[2][1] m[2][2]
@transpose
def adjoin(matrix):
    try:
        result = [[((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1])),
                   -((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0])),
                   +((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))],
                  [-((matrix[0][1] * matrix[2][2]) - (matrix[0][2] * matrix[2][1])),
                   +((matrix[0][0] * matrix[2][2]) - (matrix[0][2] * matrix[2][0])),
                   -((matrix[0][0] * matrix[2][1]) - (matrix[0][1] * matrix[2][0]))],
                  [+((matrix[0][1] * matrix[1][2]) - (matrix[0][2] * matrix[1][1])),
                   -((matrix[0][0] * matrix[1][2]) - (matrix[0][2] * matrix[1][0])),
                   +((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]))]]
    except Exception as err:
        print(err)

    return result


def det(matrix):
    try:
        # fungsi untuk menghitung determinan matrix 3x3
        result = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2])
                  - matrix[1][0] * (matrix[1][0] * matrix[2][2] - matrix[2][1] * matrix[0][2])
                  + matrix[2][0] * (matrix[0][1] * matrix[1][2] - matrix[1][1] * matrix[0][2]))
    except Exception as err:
        print(err)

    return result


def determinan(matrix):
    try:
        deter = (matrix[0][0] * matrix[1][1] * matrix[2][2]
                 + matrix[0][1] * matrix[1][2] * matrix[2][0]
                 + matrix[0][2] * matrix[1][0] * matrix[2][1]
                 - matrix[2][0] * matrix[1][1] * matrix[0][2]
                 - matrix[2][1] * matrix[1][2] * matrix[0][0]
                 - matrix[2][2] * matrix[1][0] * matrix[0][1])
    except Exception as err:
        print(err)
    return deter


# fungsi untuk mencari inverse dari matrix yang berupa nested list
def inverse(amatrix):
    multiply = lambda adj: [[(amatrix * adj[i][j]) for j in range(len(adj[0]))] for i in range(len(adj))]
    # gunakan fungsi lambda disini untuk menggantikan fungsi perkalian
    # yang mengalikan sebuah nilai tunggal x denganmatrix
    return multiply
    # fungsi ini mereturn hasil perkalian sesuai rumus
    # invers: (1/determinan A)(adjoin A)


# fungsi untuk menghitung nilai X yang merupakan perkalian inverse(A) dengan matrix B
def perkalianMatrix(function, matrix):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for row in range(len(function)):
        for col in range(len(function[0])):
            result[row][col] = function[row][col] * matrix[col]
        print(result[row])
        result[row] = reduce(lambda x, y: x + y, result[row])
        print("ini result tambah " + str(result[row]))

    return result


def result(function):
    def wrapper(*Args, **Kwargs):
        result = function(*Args, **Kwargs)
        x = result[0]
        y = result[1]
        z = result[2]
        # Isi fungsi ini sebagai decorator untuk mencetak hasil
        # Dapatkan nilai x, y, z dari function
        # Fungsi ini akan mereturn string x,y,z beserta masing" valuenya sebagaimana yang di
        return f"Nilai x, y, dan z masing - masing adalah {int(x)}, {int(y)} dan {int(z)}"

    return wrapper


@result
def get_result(matrixA, matrixB):
    result = 0
    detr = determinan(matrixA)
    print("ini determinan : " + str(detr))
    adj = adjoin(matrixA)
    print("ini adjoin : " + str(adj))
    matrixA = inverse(1 / detr)(adj)
    print("ini Inverse : " + str(matrixA))
    result = perkalianMatrix(matrixA, matrixB)
    print("ini perkalian : " + str(result))
    return result


A = [[2, 1, -1], [1, 1, 1], [1, -2, 1]]
B = [1, 6, 0]
X = get_result(A, B)
print(X)
# output = Nilai x, y, dan z masing - masing adalah 1, 2 dan 3
