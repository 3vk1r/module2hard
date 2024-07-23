while True:
    n = int(input('Введите код из первой вставки'))
    if n in range(3, 21):
        password = ''
        for i in range(1, n+1):
            for j in range(i, n+1):
                if n % (i + j) == 0 and i != j:
                    password += str(i) + str(j)
        print(password)
        break
    else: print('Такого числа не может быть в первой вставке')