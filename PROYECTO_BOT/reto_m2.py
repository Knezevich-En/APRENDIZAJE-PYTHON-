class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo_actual = saldo_inicial
    
    def depositar(self, monto):
        self.saldo_actual += monto
        print(f"Depósito de ${monto}")
        print(f"Nuevo saldo Disponible ${self.saldo_actual}")
mi_cuenta = CuentaBancaria("Arturo", 100)
mi_cuenta.depositar(50)
mi_cuenta.depositar(200)