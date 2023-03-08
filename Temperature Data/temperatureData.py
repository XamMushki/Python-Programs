
from numpy import size


def readFile():
    with open('city_temp_la.csv', 'r') as fin:
        content = fin.read()  # string
        lines = content.split('\n')  # list of strings
        # list of lists of lines splitted (individual values)
        lol_lines = []
        for line in lines:
            lol_lines.append(line.split(','))
        return lol_lines


def generateDate(data):  # data: list of lists
    result = []
    # result[][][] contains 5 lists (years)
    # each of which contains 12 lists(months)
    # each of which contains temperature data of class float/string

    # data[data_item_number][4] contains month
    # data[data_item_number][5] contains day
    # data[data_item_number][6] contains year
    # data[data_item_number][7] contains temperature of class string
    years = 5
    months = 12

    data_item_number = 1
    # acts as counter for iterating data[][], each list in data contains info about a single day
    result = []

    for i in range(years):
        list_year = []
        for j in range(months):
            list_month = []
            for k in range(31):
                # if statement used because the number of days in a month can either be 28, 29, 30, or 31
                if k+1 == int(data[data_item_number][5]):
                    # convert temperature into float for future calculations
                    list_month.append(float(data[data_item_number][7]))
                    data_item_number += 1
                else:
                    break
            list_year.append(list_month)
        result.append(list_year)
    return result


def printResult(res):
    # res[][][]
    year_no = 2015
    years = 5
    months = 12
    for i in range(years):
        print('\n\nYear: ', year_no+i)
        for j in range(12):
            print('\nMonth: ', j+1)
            x = size(res[i][j])
            pl = []
            # print(x)
            for k in range(x):
                print(result[i][j][k], end=' ')
                if (k+1) % 5 == 0:
                    print()
            print()


data = readFile()   # data: list of lists
result = generateDate(data)
printResult(result)
