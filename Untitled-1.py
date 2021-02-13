nombre = input("ingrese su nombre")
g = input("indique su genero (H o M)")
if g == "M":
    if nombre.lower() < "m" :
        g = "A"
    else: 
     g ="B"
else:
    if nombre.lower()>"n":
        g = "A"
    else: 

         grupo = "B"
print("pertenece al grupo"+g)