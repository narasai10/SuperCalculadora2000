nome = str(input('Olá, qual seu nome?\n'))
print(f'tudo bem {nome}?\n Aqui você tera a Divisão Completa')
def conta():
    num1 = int(input('Escolha um numero:\n'))
    num2 = int(input('escolha outro numero:\n'))
    print(f'O resuldado da divisão \n{num1//num2}')
    print(f'E o resto é\n{num1%num2}')
    recomeço = str(input('Vcoê gostaria de realizar uma nova conta? Diga Y para aceitar e N para negar \n'))
    if recomeço == 'Y':
        conta()
