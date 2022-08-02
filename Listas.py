print("Exercicio sobre listas")

lista = [8, 22, 14, 65, 25, 30]

num1 = int(input("Digite o Primeiro numero: "))
num2 = int(input("Digite o Segundo numero: "))
res1 = False
res2 = False
primeiro = 0
x = 0

while x < len(lista):
  if lista[x] == num1:
    res1 = True
    if not res2:
      primeiro = num1
  if num2 == lista[x]:
    res2 = True
    if not res1:
      primeiro = num2
  x += 1

if res1 == True:
  print(f"O primeiro Número foi encontrado")
else:
  print(f"O Primeiro Número NÃO foi encontrado")
if res2 == True:
  print(f"O segundo Número foi encontrado")
else:
  print(f"O segundo Número NÃO foi encontrado")

if primeiro != 0:
  print(f"O Primeiro número encontrado na lista foi o {primeiro}")
else:
  print("Nenhum Número foi encontrado")