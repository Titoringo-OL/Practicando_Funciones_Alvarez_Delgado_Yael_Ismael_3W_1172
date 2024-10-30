print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")
# 15 Pero al agregar , / obtendrá un error si intenta enviar un argumento de palabra clave:
def my_function(x, /):
    print(x)

my_function(x = 3)