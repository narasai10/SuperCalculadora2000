import DesignForPy as dfp
print(dfp.convert('DIVISAO').toCustom('larry3d'))
def  divisao():
    numero1 = int(input('digite um numero?'))
    numero2 = int(input('diga outro numero?'))
    print(numero1/numero2)
    res = int(input('outra divisao?'))   
    if res == 1:
        divisao()
    
