import os

lista_compras = []
while True:
    print("*** MAQUINA DE SNACKS ***")
    print("1. Mostrar Snacks")
    print("2. Comprar Snacks")
    print("3. Mostrar ticket")
    print("4. Vaciar Carrito")
    print("5. Salir")
    snacks = [{"id":1, "nombre":"Papas", "precio":2000}, {"id":2, "nombre":"Chocolatina", "precio":1000}, {"id":3, "nombre":"Gaseosa", "precio":1500}, {"id":4, "nombre":"Galletas", "precio":500}, {"id":5, "nombre":"Sandwich", "precio":2000}, {"id":6, "nombre":"Jugos", "precio":1500}, {"id":7, "nombre":"Agua", "precio":1000}, {"id":8, "nombre":"Chicles", "precio":500}, {"id":9, "nombre":"Mani", "precio":1000}, {"id":10, "nombre":"Chocolatina", "precio":1000}]
    
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            print("--- SNACKS DISPONIBLES ---")
            for s in snacks:
                print(f"ID: {s['id']} - Nombre: {s['nombre']} - Precio: {s['precio']}")
            os.system("pause")
            os.system("cls")

        elif opcion == 2:
            print("--- COMPRA DE SNACKS ---")
            id_snack = int(input("Ingrese el ID del snack que desea comprar: "))
            lista_compras.append(snacks[id_snack - 1])
            print(f"Se ha agregado {snacks[id_snack - 1]['nombre']} a la lista de compras.") 
            os.system("pause")
            os.system("cls")
                   
        elif opcion == 3:
            total = 0
            print(f"--- TICKET DE COMPRA ---")
            for i in lista_compras:
                print(f"ID: {i['id']} - Nombre: {i['nombre']} - Precio: ${i['precio']}")
                total += i['precio']
            print(f"Total: ${total}")
            os.system("pause")
            os.system("cls")

        elif opcion == 4:
            lista_compras = []
            print("Carrito vaciado.")
            os.system("pause")
            os.system("cls")
            
        elif opcion == 5:
            print("Gracias por su compra.")
            break
            
    except ValueError:
        print("Error: Ingrese un número válido.")
        continue
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        break



