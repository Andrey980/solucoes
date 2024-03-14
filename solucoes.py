# 1) Observe o trecho de código abaixo:

indice = 13
soma = 0
k = 0

while k < indice:

    k += 1

    soma += k

print(soma)
# Ao final do processamento, qual será o valor da variável SOMA? 91


# 2)

def verifica_fibonacci(numero):
    # Inicializa a sequência de Fibonacci com os dois primeiros valores
    fibonacci_sequencia = [0, 1]

    while fibonacci_sequencia[-1] < numero:
        next_value = fibonacci_sequencia[-1] + fibonacci_sequencia[-2]
        fibonacci_sequencia.append(next_value)

    if numero in fibonacci_sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."


numero_informado = int(input("Digite um número: "))
print(verifica_fibonacci(numero_informado))


# 3) Descubra a lógica e complete o próximo elemento:

# a) 1, 3, 5, 7, 9

# b) 2, 4, 8, 16, 32, 64, 128

# c) 0, 1, 4, 9, 16, 25, 36, 49

# d) 4, 16, 36, 64, 100

# e) 1, 1, 2, 3, 5, 8, 13

# f) 2,10, 12, 16, 17, 18, 19, 20


# 4)...


# 5)

def inverter_string(string):
    inv_string = ""
    for i in range(len(string) - 1, -1, -1):
        inv_string += string[i]
    return inv_string


string_original = input("Digite uma palavra: ")
print(inverter_string(string_original))
print("String original:", string_original)
