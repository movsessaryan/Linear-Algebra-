from fractions import Fraction
fr = Fraction
fr.__repr__ = fr.__str__

def norm(matrix , ind):
    for i in range(ind+1,len(matrix)):
        if matrix[i][ind] != 0:
            matrix[ind],matrix[i] = matrix[i],matrix[ind]
def z(matrix, ind):
    for i in range(ind+1,len(matrix)):
        alpha = matrix[i][ind]/matrix[ind][ind]
        for j in range(len(matrix[0])):
            matrix[i][j] -= alpha*matrix[ind][j]

def gaus(matrix,f=z):
    n = min(len(matrix), len(matrix[0]))
    for i in range(n):
        norm(matrix,i)
        f(matrix,i)


def normalize(row):
    m = 1    
    for item in row:
        m *= item.denominator

    for i in range(len(row)):
        row[i] *= m

    t = [x.numerator for x in row]
    g = gcd_aray(t)
    if g == 0:
        return
    for i in range(len(row)):
        row[i] /= g

def gcd_aray(arr):
    def temp(start):
        if start == len(arr) -1:
            return arr[len(arr) -1]
        return gcd(arr[start],temp(start+1))
    return temp(0)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)


matrix = [[fr(12),fr(13),fr(12)],[fr(1),fr(123),fr(0)],[fr(12),fr(23),fr(3)], [fr(12),fr(23),fr(3)], [fr(10),fr(22),fr(31)]]
gaus(matrix)
for item in matrix:
    normalize(item)
    print (item)
 