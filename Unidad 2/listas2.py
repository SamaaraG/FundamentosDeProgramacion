#Crear una lista vacia con nombre y agregar cinco elementos 
#con input: (Nombre, preparatoria, lugar de residencia, edad, carrera)

listas2 = []

print(listas2)
print("👉 Lista de estudiantes TecNM Pabellon")

#Agregar datos
dato1 = input(" ⭐Nombre: ")
listas2.append(dato1)

dato2 = input(" ⭐Preparatoria: ")
listas2.append(dato2)

dato3 = input(" ⭐Lugar de residencia: ")
listas2.append(dato3)

dato4 = input(" ⭐Edad: ")
listas2.append(dato4)

dato5 = input(" ⭐Carrera: ")
listas2.append(dato5)

print("\n📖 La lista de estudiantes se presenta a continuacion: 📖")

for dato in listas2:
    print(f"- {dato1, dato2, dato3, dato4, dato5}")

print("\n✅ ¡Lista creada con éxito!")

