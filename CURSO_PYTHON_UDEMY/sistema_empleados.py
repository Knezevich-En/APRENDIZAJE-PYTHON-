nombre_empleado = input("Ingrese su nombre: ")
edad_empleado = int(input("Ingrese su edad: "))
salario_empleado = float(input("Ingrese su salario: $"))
jefe_departamento = input("¿Es jefe de departamento? (Si/No): ")

jefe_departamento = jefe_departamento.lower().strip() == 'si'

print("Nombre: ", nombre_empleado)
print("Edad: ", edad_empleado)
print("Salario: ", salario_empleado)
print(f"Es jefe de departamento? {jefe_departamento}")