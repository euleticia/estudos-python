# Projeto impar ou par
while True:
  try:
    valor = int(input("Digite um numero:"))
    if valor % 2 == 0:
      print("O numero eh par")
    else:
      print("O numero eh impar")
  except:
    print('Digite apenas numeros')