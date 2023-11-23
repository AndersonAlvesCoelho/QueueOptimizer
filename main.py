# Tenho uma lista de 5 número (1 a 5) e preciso que cada número passe pelas seguintes funções (A, B, C, D), 
# um número não pode passar pela função seguinte sem passar pela anterior (não pode passar por B, sem passar em A).

# Preciso de um algoritmo que faça com que ao rodar o programa, assim que o 1° número (1) entrar na função (A) e 
# terminar e for para (B), que o próximo número (2) já entre na função (A) otimizando assim o tempo para que não seja 
# preciso que o 1° número passe por todas as funções e quando completar a função (D) que o 2° rode em (A)

# A ideia seria tipo várias filas, onde cada função fica esperando dados para executar e que se filas sejam criadas em cada uma das funções

from queue import Queue

# Função A
def func_A(number):
    print(f"Função A: Processando número {number}")

# Função B
def func_B(number):
    print(f"Função B: Processando número {number}")

# Função C
def func_C(number):
    print(f"Função C: Processando número {number}")

# Função D
def func_D(number):
    print(f"Função D: Processando número {number}")

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Fila para cada função
fila_A = Queue()
fila_B = Queue()
fila_C = Queue()
fila_D = Queue()

# Adiciona números à fila A
for numero in numeros:
    fila_A.put(numero)

# Processa as filas
while not fila_A.empty():
    numero = fila_A.get()
    func_A(numero)
    fila_B.put(numero)  # Adiciona o número à fila B
    func_B(numero)
    fila_C.put(numero)  # Adiciona o número à fila C
    func_C(numero)
    fila_D.put(numero)  # Adiciona o número à fila D
    func_D(numero)

# Quando a fila A estiver vazia, processa as filas B, C e D
while not fila_B.empty():
    numero = fila_B.get()
    func_A(numero)

while not fila_C.empty():
    numero = fila_C.get()
    func_A(numero)

while not fila_D.empty():
    numero = fila_D.get()
    func_A(numero)



# def A(num):
#     print("------------------------")
#     print(num)
#     print("A")
    

# def B(num):
#     print("------------------------")
#     print(num)
#     print("B")

# def C(num):
#     print("------------------------")
#     print(num)
#     print("C")

# def D(num):
#     print("------------------------")
#     print(num)
#     print("D")

# def switch_function(fun, num):
    
#     if fun == 'A':
#         A(num)
#     elif fun == 'B':
#         B(num)
#     elif fun == 'C':
#         C(num)
#     elif fun == 'D':
#         D(num)
#     else: 
#         "You're too young to party"


# list_number = [1, 2, 3, 4, 5]
# list_function = ['A', 'B', 'C', 'D']



# for num in list_number:
#     for fun in list_function: 
#         switch_function(fun, num)