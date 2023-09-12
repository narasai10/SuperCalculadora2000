nome = str(input('Qual seu nome: '))
def somar():
    prg1 = float(input('Escolha um número para somar: '))
    prg2 = float(input('Escolha outro número para somar: '))
    produto = (prg1 + prg2)
    print(f'O produto é: {produto}')
    recomeço = str(input('Gostaria de realizar outra soma? Digite "S" para sim ou digite "N" para não: '))
    if recomeço == 'S':
        somar()
