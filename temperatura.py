def celsius_a_fahrenheit(celsius):
  
  """Convierte grados Celsius a grados Fahrenheit."""
  
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_a_celsius(fahrenheit):

  """Convierte grados Fahrenheit a grados Celsius."""
  
  celsius = (fahrenheit - 32) * 5/9
  return celsius

while True:
  print("Conversor de Temperatura")
  print("1. Celsius a Fahrenheit")
  print("2. Fahrenheit a Celsius")
  print("3. Salir")

  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    try:
      celsius = float(input("Ingrese la temperatura en grados Celsius: "))
      fahrenheit = celsius_a_fahrenheit(celsius)
      print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.\n")
    except ValueError:
      print("Entrada inválida. Por favor, ingrese un número.\n")
  elif opcion == '2':
    try:
      fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
      celsius = fahrenheit_a_celsius(fahrenheit)
      print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.\n")
    except ValueError:
      print("Entrada inválida. Por favor, ingrese un número.\n")
  elif opcion == '3':
    print("¡Gracias por usar el conversor de temperatura!")
    break
  else:
    print("Opción inválida. Por favor, seleccione 1, 2 o 3.\n")
