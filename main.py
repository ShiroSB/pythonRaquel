def main():

    lista = list()
    code = codee()
    i = 0
    k = 2
    z = 3
    x = int(input("Introduce la cantidad de registros que quieres ingresar"))
    while x < 1:
     x = int(input("Introduce la cantidad de registros que quieres ingresar"))
    for y in range(x):
        nombre = (input("Introduce tu nombre : "))
        lista.append(nombre[:2])
        apellido = (input("Introduce tu apellido : "))
        lista.append(apellido[:2])
        apellido2 = (input("Introduce tu 2do apellido : "))
        code.append(nombre[:2]+apellido[:2]+apellido2[:2])
        telefono.append(input("Introduce tu telefono : "))
        edad.append(int(input("Introduce tu edad : ")))
        contacto = (int(input("Contacto T/F")))
    while contacto < 0 or contacto > 1:
         contacto = (int(input("Contacto T/F")))
    lista.append(contacto)

    while i < x:
        print(lista[k:z])
        k += 6
        z += 6
        i += 2

if __name__ == '__main__':
       main()
