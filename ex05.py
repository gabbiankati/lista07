import random

sorteio = random.randint(0, 100)
acertou = False

for i in range(10):
    palpite = int(input('Informe seu palpite: '))

    if palpite == sorteio:
        acertou = True
        print(f'Parabéns! Você acertou em {i + 1} tentativas!')
        break
    else:
        print('Erroooooooouuuu! Tenta de novo, eltão')

if acertou == False:
    print(f'O número sorteado foi {sorteio}')

