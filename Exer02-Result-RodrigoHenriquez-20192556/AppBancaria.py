from ClassesApp import Cuenta, Egresos, Ingresos, menu

cuenta = 0.0
RegistroEgresos = []
RegistroIngresos = []

while True:
    menu()
    option = int(input("Escoja una opcion: "))

    if option == 0:
        break

    elif option == 1:
        Retiro = float(input("Cuanto desea retirar: "))
        RegistroEgresos.append(Retiro)
        RetiroPrimero = Egresos(Retiro)
        Resultado = RetiroPrimero.retiroNuevo()
        cuenta = cuenta + Resultado
        print("El monto en su cuenta es de " + str(cuenta) + " dolares")
        print("----------------------------")

    elif option == 2:
        Deposito = float(input("Cuanto desea depositar: "))
        RegistroIngresos.append(Deposito)
        DepositoPrimero = Ingresos(Deposito)
        Resultado = DepositoPrimero.nuevoIngresos()
        cuenta = cuenta + Resultado
        print("El monto en su cuenta es de " + str(cuenta) + " dolares")
        print("----------------------------")

    elif option == 3:
        print("Sus retiros han sido los siguientes:")
        for registroRe in RegistroEgresos:
            print(registroRe)

        sumaDeRetiro = 0.0
        for registroRe in RegistroEgresos:
            sumaDeRetiro = sumaDeRetiro + registroRe

        cantidadReg = len(RegistroEgresos)

        print(
            "Ustede ha realizado la cantidad de "
            + str(cantidadReg)
            + (" registros, con un total de: $")
            + str(sumaDeRetiro)
        )

    elif option == 4:
        print("Sus depositos han sido los siguientes:")
        for registroDe in RegistroIngresos:
            print(registroDe)

        sumaDeDeposito = 0.0
        for registroDe in RegistroIngresos:
            sumaDeDeposito = sumaDeDeposito + registroDe

        cantidadDep = len(RegistroIngresos)

        print(
            "Ustede ha realizado la cantidad de "
            + str(cantidadDep)
            + (" depositos, con un total de: $")
            + str(sumaDeDeposito)
        )

    elif option == 5:
        print("Sus retiros han sido los siguientes:")
        for registroRe in RegistroEgresos:
            print(registroRe)

        print("Sus depositos han sido los siguientes:")
        for registroDe in RegistroIngresos:
            print(registroDe)

        cantidadReg = len(RegistroEgresos)
        cantidadDep = len(RegistroIngresos)
        numTrans = cantidadDep + cantidadReg

        sumaDeRetiro = 0.0
        for registroRe in RegistroEgresos:
            sumaDeRetiro = sumaDeRetiro + registroRe

        sumaDeDeposito = 0.0
        for registroDe in RegistroIngresos:
            sumaDeDeposito = sumaDeDeposito + registroDe

        totalMovidos = sumaDeDeposito + sumaDeRetiro

        print(
            "Usted ha realizado la cantidad de "
            + str(numTrans)
            + " transacciones. Usted han movido: $"
            + str(totalMovidos)
        )

    elif option == 6:
        print("El saldo actual de su cuenta es de: $" + str(cuenta))
