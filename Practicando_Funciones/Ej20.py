print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")
#20
#Recursividad
#Python también acepta la recursividad de funciones, lo que significa que una función definida puede llamarse a sí misma.

#La recursividad es un concepto matemático y de programación común. Significa que una función se llama a sí misma. Esto tiene la ventaja de que puede recorrer los datos para llegar a un resultado.

#El desarrollador debe tener mucho cuidado con la recursividad, ya que puede ser bastante fácil escribir una función que nunca termina, o una que utiliza cantidades excesivas de memoria o potencia del procesador. Sin embargo, cuando se escribe correctamente, la recursividad puede ser un enfoque de programación muy eficiente y matemáticamente elegante.

#En este ejemplo, tri_recursion() es una función que hemos definido para llamarse a sí misma ("recurse"). Usamos la variable k como datos, que disminuye (-1) cada vez que recurrimos. La recursividad finaliza cuando la condición no es mayor que 0 (es decir, cuando es 0).

#A un nuevo desarrollador le puede llevar algún tiempo descubrir cómo funciona exactamente esto; la mejor manera de averiguarlo es probándolo y modificándolo.

#Ejemplo



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")