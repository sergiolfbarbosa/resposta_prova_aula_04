#   [LP-A04] Escreva um programa em python que leia números inteiros do teclado. 
#   O programa deve ler os números até que o usuário digite 0 (zero). 
#   No final da execução, exiba a quantidade de números
#   digitados, assim como a soma e a média aritmética.

count = 0
numero = 1
soma = 0
media = 0
for i in range(999):
    while numero != 0:
        print ("Para encerrar aperte o dígito ( 0 )-ZERO e tecle ENTER!")
        numero = int(input("Digite um número inteiro : "))
        count += 1
        soma = soma + numero
count = count - 1 # linha inclusa para remover o "0" da contagem, pois daria erro no cálculo da média.
media = soma / count
print (f"A quantidade de números digitados é {count}.")
print (f"A soma dos números digitados é {soma}.")
print (f"A média dos números digitados é {media}.")

    