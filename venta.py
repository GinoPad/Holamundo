x = 1
while x > 0:
    nombre_producto = input("Introduzca nombre del producto a llevar: ")

    precio_producto = int(input("Introduzca el precio del producto: "))

    cantidad_producto = int(input("Cuántos productos se está llevando?"))

    precio_total = cantidad_producto * precio_producto

    print(f"Usted se lleva una cantidad de {cantidad_producto} de {nombre_producto} a un precio total de {precio_total}")
   
    x = int(input("Desea continuar? 0 para no | 1 para si"))
    if x == 1:
        
        nombre_producto = input("Introduzca nombre del producto a llevar: ")

        precio_producto = int(input("Introduzca el precio del producto: "))

        cantidad_producto = int(input("Cuántos productos se está llevando?"))

        print(f"Usted se lleva una cantidad de {cantidad_producto} de {nombre_producto} a un precio total de {precio_total}")

        x = int(input("Desea continuar? 0 para no | 1 para si"))
    elif x == 0:
        print("Compra finalizada")
    

