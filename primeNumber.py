def primeUsingWhile(num):
    if num < 2:
        print(num, 'is not a prime number.')
    elif num > 1:
        i = 2
        flag = True
        while i < num:
            if num % i == 0:
                flag = False
                break
            i += 1
        if flag == True:
            print(num, 'is a prime number.')
        else:
            print(num, 'is not a prime number.')


def primeUsingFor(num):
    if num < 2:
        print(num, 'is not a prime number.')
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, 'is not a prime number.')
                break
        else:
            # executes only if the break statement in for loop does not execute
            print(num, 'is a prime number.')


if __name__ == '__main__':
    num = int(input('Enter Number: '))
    primeUsingWhile(num)
    primeUsingFor(num)
