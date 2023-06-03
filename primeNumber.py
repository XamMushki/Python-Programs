num = int(input('Enter Number: '))
if num == 1:
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
