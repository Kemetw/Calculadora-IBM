# Definimos a variável inicial para entrar no loop
continuar = "s"

while continuar == "s":
    print("\n--- Calculadora de IBM ---")
    
    # Pedimos os dados de forma clara
    peso = float(input("Peso = 80.5 (kg): "))
    altura = float(input("Altura = 1.75 (m): "))
    
    # Fazemos o cálculo
    imc = peso / (altura ** 2)
    
    # Mostramos o resultado
    print(f"Seu IBM é: {imc:.2f}")
    
    # Lógica de decisão
    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 25:
        print("Classificação: Peso ideal")
    else:
        print("Classificação: Sobrepeso")
        
    # Pergunta se quer repetir
    continuar = input("\nDeseja calcular novamente? (s/n): ")

print("Programa encerrado. Até mais!")   
