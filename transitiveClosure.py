# Using Warshall's algorithm
def printMatrix(matrix):
    for l in matrix:
        print(l)
    print('')


def findTransitiveClosure(tc_matrix, size):
    for i in range(size):
        # stores the indices of the elements at whatever place there is 1 in a column
        col_with_ones = []
        # stores the indices of the elements at whatever place there is 1 in a row
        row_with_ones = []
        for j in range(size):
            if tc_matrix[j][i] == 1:  # checks, if there is 1 in the current column
                col_with_ones.append(j)
            if tc_matrix[i][j] == 1:  # checks, if there is 1 in the current row
                row_with_ones.append(j)

        # changing the values for better understanding, only for displaying purpose
        temp_col = []
        temp_row = []
        for element in col_with_ones:
            temp_col.append(element+1)
        for element in row_with_ones:
            temp_row.append(element+1)
        print(f'C{i+1}: ', end='')
        print(temp_col)
        print(f'R{i+1}: ', end='')
        print(temp_row)
        print('New Ordered Pairs: ', end='')
        for l in col_with_ones:
            for m in row_with_ones:
                print(f'({l+1},{m+1})', end=', ')    # new ordered pairs
                # assigning 1's at the newly formed combinations/Ordered pairs
                tc_matrix[l][m] = 1

        if (i == size-1):
            print('\nTransitive Closure of the Matrix MR1 is:', end='')
        print(f'\nW{i+1}: ')
        printMatrix(tc_matrix)


def getMatrix():
    size = int(input('Enter Set A size: '))

    # The matrix will be 'size x size'
    matrix_r1 = []
    print(
        f'Enter elements(1\'s/0\'s) of MR1, one row at a time - {size} elements separated by commas \',\':')
    for i in range(size):
        temp_str = input(f'Row{i+1}: ')
        temp_list = temp_str.split(',')
        temp_list = list(map(int, temp_list))
        matrix_r1.append(temp_list)
    return matrix_r1, size


matrix_r1, size = getMatrix()
print('W0: ')
printMatrix(matrix_r1)
findTransitiveClosure(matrix_r1, size)
