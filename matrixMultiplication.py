class MatrixMultiplication:
    def __init__(self) -> None:
        self.m = int(input('Enter Number of Rows in M1: '))
        self.n = int(input('Enter Number of Columns in M1: '))
        self.k = int(input('Enter Number of Columns in M2: '))
        self.m1 = []     # of size mxn (Row x Col)
        self.m2 = []     # of size nxk

        self.new_matrix = []  # mxn

        print('Enter M1 Elements: ')
        for i in range(self.m):
            temp_row = []
            for j in range(self.n):
                temp_item = int(input('M'+str(i)+str(j)+': '))
                temp_row.append(temp_item)
            self.m1.append(temp_row)

        print('Enter M2 Elements: ')
        for i in range(self.n):
            temp_row = []
            for j in range(self.k):
                temp_item = int(input('M'+str(i)+str(j)+': '))
                temp_row.append(temp_item)
            self.m2.append(temp_row)

    def multiple(self):
        for i in range(self.m):
            new_row = []
            for j in range(self.k):
                new_item = 0
                for l in range(self.n):
                    temp_item = self.m1[i][l] * self.m2[l][j]
                    new_item += temp_item
                new_row.append(new_item)
            self.new_matrix.append(new_row)

    def printMatricies(self):
        print('M1: ')
        for row in self.m1:
            print(row)

        print('M2: ')
        for row in self.m2:
            print(row)

        print('     RESULT\nM1 x M2: ')
        for row in self.new_matrix:
            print(row)


if __name__ == '__main__':
    m = MatrixMultiplication()
    m.multiple()
    m.printMatricies()
