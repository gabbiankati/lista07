num = int(input('Informe um número: '))

for i in range(1, num):
    if i % 3 == 0 or i % 7 == 0:
        print('*')
    else:
        print(i)