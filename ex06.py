num = int(input('Informe um número inteiro: '))
primo = True

for i in range(2, num):
    if num % i == 0:
        primo = False
        break

if primo:
    print('É primo!')
else:
    print('Não é primo!')