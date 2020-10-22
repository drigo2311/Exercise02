from unittest import result


class Cuenta:
    def __init__(self):
        self.cuentaNueva = 0.0

    def Total(self):
        self.cuentaNueva = result
        return result


class Egresos:
    def __init__(self, Retiro):
        Cuenta.__init__(self)
        self.NuevoEgreso = Retiro

    def retiroNuevo(self):
        self.cuentaNueva = self.cuentaNueva - self.NuevoEgreso
        return self.cuentaNueva


class Ingresos:
    def __init__(self, Deposito):
        Cuenta.__init__(self)
        self.NuevoIngreso = Deposito

    def nuevoIngresos(self):
        self.cuentaNueva = self.cuentaNueva + self.NuevoIngreso
        return self.cuentaNueva


def menu():
    print("----------------------------")
    print("Programa Bacancario de cuentas personales")
    print("¿Qué actividad quiere realizar?")
    print("Digite el número de la opción que desea")
    print("0. Salir del programa")
    print("1. Retirar Dinero")
    print("2. Depositar Dinero")
    print("3. Registros de retiros")
    print("4. Registro de depósitos")
    print("5. Ver todas las transacciones")
    print("6. Saldo en la cuenta")
