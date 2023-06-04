def fibonacciSeq(n):
    c = 1
    c_prev = 0
    print('Fibonacci Sequence: ', end='')
    for i in range(n):
        print(c, end=', ')
        temp = c
        c += c_prev
        c_prev = temp
    print()


if __name__ == '__main__':
    n = int(input("Enter n: "))
    fibonacciSeq(n)
