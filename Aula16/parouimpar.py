

numero_inteiro = input("Digite um número inteiro: ")
"""
if not numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
          print(f"{numero_inteiro} é par.")
    else:
          print(f"{numero_inteiro} é impar")
else:
      print ("Isso não é um inteiro.")
"""

if not numero_inteiro.isdigit():
  print("Isso não é um numero inteiro.")
else:
  numero_inteiro = int(numero_inteiro)

  if not numero_inteiro % 2 == 0:
        print(f"{numero_inteiro} é impar")
  else:
        print(f"{numero_inteiro} é par")
