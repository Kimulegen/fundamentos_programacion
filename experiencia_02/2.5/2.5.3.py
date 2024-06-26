#! Python
# Credit card simulator

# initialize variables
saldo = -100000

# menu
while True:
    try:
        print("Seleccione una opción")
        print("1. Pago de tarjeta de crédito")
        print("2. Simular compras")
        print("3. Salir")
        opt = int(input("Ingrese su opción"))

        # pay debt
        if opt == 1:
            try:
                monto_pago = int(input("Ingrese un monto a pagar: "))
            except ValueError as ve:
                print(ve)
                print("Monto ingresado es invalido")
                break
            if monto_pago < 0:
                print("El monto ingresado debe ser un número positivo")
            elif monto_pago > saldo:
                print("El monto ingresado excede el monto actual de la tarjeta")
            else:
                saldo += monto_pago

        # shopping simulator
        elif opt == 2:
            total_compra = 0
            while True:
                try:
                    compra = int(
                        input("Ingrese el monto de la compra (Ingrese 0 para salir)")
                    )
                except ValueError as ve:
                    print("Monto ingresado a comprar invalida")
                else:
                    if compra == 0:
                        if compra >= 0:
                            saldo -= compra
                            print(
                                f"Se hizo una compra por el monto total de {total_compra}, su nuevo saldo es de {saldo}"
                            )
                    elif compra >= 0:
                        total_compra += compra
                        print("Compra realizada con exito")
                    else:
                        print("El monto de la compra debe ser un numero positivo")

        # exit menu
        elif opt == 3:
            print("adios")
            break

        # handle invalid inputs
        else:
            print("Por favor ingresar una opción válida")

    # handle exceptions
    except ValueError as ve:
        print(ve)
        print("La opción ingresada no es válida")
        break
