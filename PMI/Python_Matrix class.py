from sys import stdin


def make_list_from_matrix(_arr):
    s = str(_arr)
    arr_s = list(map(str, s.split('\n')))
    arr = []
    for i in arr_s:
        arr.append(i.split('\t'))
    arr_int = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr_int[i][j] = int(arr[i][j])
    return arr_int


class Matrix:
    def __init__(self, _arr):
        import copy
        self.arr = copy.deepcopy(_arr)

    def __str__(self):
        self.str = ''
        if isinstance(self.arr, Matrix):
            self.arr = make_list_from_matrix(self.arr)
        if len(self.arr) == 0:
            return self.str
        for i in range(len(self.arr) - 1):
            self.str += '\t'.join(str(x) for x in self.arr[i])
            self.str += '\n'
        self.str += '\t'.join(str(x) for x in self.arr[-1])
        return self.str

    def __add__(self, _new_arr):
        arr = make_list_from_matrix(_new_arr)
        if len(self.arr) != len(arr):
            raise MatrixError(Matrix(self.arr), _new_arr)
        base_length = len(self.arr[0])
        for i in range(len(self.arr)):
            if len(self.arr[i]) != base_length or len(arr[i]) != base_length:
                raise MatrixError(Matrix(self.arr), _new_arr)
        new_arr = [[0 for _ in range(len(self.arr[0]))] for _ in range(len(self.arr))]
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                new_arr[i][j] = self.arr[i][j] + arr[i][j]
        return Matrix(new_arr)

    def __mul__(self, _a):
        if isinstance(self.arr, Matrix):
            self.arr = make_list_from_matrix(self.arr)
        if isinstance(_a, int) or isinstance(_a, float):
            new_arr_alpha = [[0 for _ in range(len(self.arr[0]))] for _ in range(len(self.arr))]
            for i in range(len(self.arr)):
                for j in range(len(self.arr[i])):
                    new_arr_alpha[i][j] = self.arr[i][j] * _a
            return Matrix(new_arr_alpha)
        else:
            if isinstance(_a, Matrix):
                arr = make_list_from_matrix(_a)
            for i in range(len(self.arr)):
                if len(self.arr[i]) != len(arr):
                    raise MatrixError(Matrix(self.arr), _a)
            ans = [[0 for _ in range(len(arr[0]))] for _ in range(len(self.arr))]
            for i in range(len(self.arr)):
                for j in range(len(arr[i])):
                    t = 0
                    for k in range(len(arr)):
                        t += self.arr[i][k] * arr[k][j]
                    ans[i][j] = t
            return Matrix(ans)

    __rmul__ = __mul__

    def transpose(self):
        new_arr = list(zip(*self.arr))
        self.arr = new_arr
        return Matrix(new_arr)

    @staticmethod
    def transposed(_arr):
        arr = make_list_from_matrix(_arr)
        return Matrix(list(zip(*arr)))

    def size(self):
        return len(self.arr), len(self.arr[0])

    def solve(self, _a):
        ans = [0 for _ in range(len(_a))]
        arr = self.arr
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(i, len(arr)):
                    arr[j][k] -= arr[i][k] * arr[j][i] / arr[i][i]
        j = len(_a) - 1
        # print(arr)
        # print(_a)
        for i in range(len(arr) - 1, -1, -1):
            x = 0
            for k in range(len(arr[i]) - 1, j, -1):
                if arr[i][k] != 0:
                    x -= ans[k] / arr[i][k]
            for k in range(j, -1, -1):
                if arr[i][k] != 0:
                    x += _a[k] / arr[i][k]
            ans[j] = x
            j -= 1
        for i in range(len(ans)):
            t = 0
            for j in range(len(ans)):
                t += ans[j] * arr[i][j]
            if t != _a[i]:
                raise Exception()
        return ans


class SquareMatrix(Matrix):
    def __pow__(self, n):
        if n == 0:
            arr = [[0 for _ in range(len(self.arr))] for _ in range(len(self.arr))]
            for i in range(len(arr)):
                arr[i][i] = 1
            return Matrix(arr)
        if n % 2 == 1:
            return Matrix(self.__pow__(n - 1) * Matrix(self.arr))
        else:
            arr = self.__pow__(n // 2)
            return Matrix(arr * arr)


class MatrixError(BaseException):
    def __init__(self, _matrix1, _matrix2):
        self.matrix1 = _matrix1
        self.matrix2 = _matrix2


exec(stdin.read())
