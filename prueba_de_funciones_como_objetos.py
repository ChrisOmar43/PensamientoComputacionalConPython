"""def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    return resultados

nums = [4, 8, 6]

print(aplicar_operacion(multiplicar_por_dos, nums)) """

multiplicar_por_dos = lambda n: n * 2

sumar_2 = lambda n: n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
    return resultados

nums = [2, 5, 8]

print(aplicar_operacion(multiplicar_por_dos, nums))