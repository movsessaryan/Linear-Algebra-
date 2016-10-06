
''' Gaus's algorithm '''
def norm(matrix, ind):
    for i in range(ind + 1, len(matrix)):
        if matrix[i][ind] != 0:
            matrix[ind], matrix[i] = matrix[i], matrix[ind]


def z(matrix, ind):
    for i in range(ind + 1, len(matrix)):
        b = matrix[i][ind]
        a = matrix[ind][ind]
        g = gcd(a,b)
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix[i][j]*(a//g) - matrix[ind][j] * (b//g)


def gaus(matrix, f=z):
    n = min(len(matrix), len(matrix[0]))
    for i in range(n):
        norm(matrix, i)
        f(matrix, i)


def normalize(row):
    g = gcd_array(row)
    if g == 0 or g == 1:
        return
    for i in range(len(row)):
        row[i] /= g


def gcd_array(arr):
    def temp(start):
        if start == len(arr) - 1:
            return arr[len(arr) - 1]
        return gcd(arr[start], temp(start + 1))

    return temp(0)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def logranj(matrix, ind):
    assert len(matrix) == len(matrix[0]), 'the matrix mast be square'
    for i in range(ind+1 ,len(matrix)):
        a = matrix[ind][ind]
        b = matrix[i][ind]
        g = gcd(a,b)
        k1 = b/g;
        k2 = a/g;
        for j in range(len(matrix)):
            matrix[i][j] = matrix[i][j]*k2 - matrix[ind][j]*k1
        '''do same for coulumns'''
        for j in range(len(matrix)):
            matrix[j][i] = matrix[j][i]*k2 - matrix[j][ind]*k1

matrix = [[12,13,12],[1,123,0],[12,23,3]]
gaus(matrix,logranj)

for item in matrix:
    normalize(item)
    print (item)
