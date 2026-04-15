class EmpleadoRobot:
    def __init__(self, nombre, asignacion):
        self.nombre_robot = nombre
        self.area_trabajo = asignacion


obrero_1 = EmpleadoRobot("Arturito-X", "Contabilidad")

print(obrero_1.nombre_robot)