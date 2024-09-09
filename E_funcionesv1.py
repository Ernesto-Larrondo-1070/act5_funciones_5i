print("Manejo de funciones v1")
def hola_mundo():
    print("Hola aqui estoy")
    print("Hola me vez")
def meza(msg):
    print(msg)
def escribeNC(Nombre, apellido):
    print(Nombre, apellido)
    print(f"tu nombre completo es {Nombre} {apellido}")
# lamando a la funcion
hola_mundo()
meza("hey mira que tal") #llama a meza con un parametro
meza("nava me sorprende cada dia mas") # llama a meza
escribeNC("Larrondo", "Ernesto")
print("funciones que rergresan valores")
def suma2numeros(n1, n2):
    s=n1+n2
    return f"la suma de {n1} y de {n2} es",s
print(suma2numeros(7,3))
print(suma2numeros(15,64))