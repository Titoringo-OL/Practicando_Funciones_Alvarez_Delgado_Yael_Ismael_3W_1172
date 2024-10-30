print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")
#19
#Combine solo posicional y solo palabras clave
#Puede combinar los dos tipos de argumentos en la misma función.

#Cualquier argumento antes de / es solo posicional y cualquier argumento después de * es solo de palabra clave.
def my_function(a, b, /, *, c, d):
 print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
