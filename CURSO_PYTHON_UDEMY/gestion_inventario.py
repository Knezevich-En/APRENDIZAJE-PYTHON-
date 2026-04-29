import os

USER_ADMIN = "admin"
PASS_ADMIN = "admin"

print("**** Gestión de Inventario ****")

inventario = []

while True:
    print("\nMenú Principal:")
    print("1. Agregar Producto/s")
    print("2. Eliminar Producto/s")
    print("3. Ver Inventario")
    print("4. Actualizar Producto/s")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad_productos = int(input("¿Cuántos productos desea agregar?: "))
        for i in range(cantidad_productos):
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            print("Producto agregado exitosamente.")
        os.system("pause")
        os.system("cls")
    elif opcion == "2":
        cantidad_productos_eliminar = int(input("¿Cuántos productos desea eliminar?: "))
        producto_eliminar = input("Nombre del producto a eliminar: ")
        for i in range(cantidad_productos_eliminar):
            for x in inventario:
                if x["nombre"] == producto_eliminar:
                    inventario.remove(x)
                    
                else: 
                    continue
            os.system("pause")
            os.system("cls")
            print("Producto eliminado exitosamente.")

    elif opcion == "3":
        for i in inventario:
            print(f"Nombre: {i['nombre']}")
            print(f"Precio: {i['precio']}")
            print(f"Cantidad: {i['cantidad']}")
            print("-" * 20)
        os.system("pause")
        os.system("cls")
    elif opcion == "4":
        cantidad_productos_actualizar = int(input("¿Cuántos productos desea actualizar?: "))
        for i in range(cantidad_productos_actualizar):
            producto_actualizar = input("Nombre del producto a actualizar: ")
            for x in inventario:
                if x['nombre'] == producto_actualizar:
                    detalle = input("¿Qué detalle desea actualizar? (nombre, precio, cantidad): ")
                    if detalle == "nombre":
                        x['nombre'] = input("Nuevo nombre: ")
                    elif detalle == "precio":
                        x['precio'] = float(input("Nuevo precio: "))
                    elif detalle == "cantidad":
                        x['cantidad'] = int(input("Nueva cantidad: "))
                    else:
                        print("Detalle no válido.")
                    print("Producto actualizado exitosamente.")
                    os.system("pause")
                    os.system("cls")
                else:
                    print("Producto no encontrado.")
                    os.system("pause")
                    os.system("cls")
                    continue                
    elif opcion == "5":
        usuario_admin = input("Usuario: ")
        password_admin = input("Password: ")
        if usuario_admin == USER_ADMIN and password_admin == PASS_ADMIN:
            print("Acceso concedido. \nCerrando programa...")
            break
        else:
            print("Acceso denegado.")
            os.system("pause")
            os.system("cls")
            continue
        
    else:
        print("Opción no válida.")
        os.system("pause")
        os.system("cls")

