import sys
print('Escolha uma das quatro operações, abaixo para começar a fazer os calculos')
op = input('+, -, *, ou / \n')
n1 = int(input('Insira o 1° valor\n'))
n2 = int(input('Insira o 2° valor\n')) 
if op == '+':
    res = n1 + n2
elif op == '-':
    res = n1 - n2
elif op == '*':
    res = n1 * n2
elif op == '/':
    res = n1 / n2
else:
    print('Você não inseriu um expressão aritmética, por favor tente novamente!')
    sys.exit()
print('O resultado é {}'.format(res) )
