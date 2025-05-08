# *Cálculo de Bônus com Entrada do Usuário*

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bônus: "))

# 4) Calcule o valor do bônus final
constante_bonus = 1000
valor_bonus = constante_bonus + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bônus
print(f"O usuário {nome_usuario} possue o bônus de  {valor_bonus}")

