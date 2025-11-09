# 1. Variables de Estado Inicial
saldo = 1000.00  # Saldo inicial de la cuenta
pin_correcto = "1234"  # PIN para simular la seguridad
intentos = 3

print("--- BIENVENIDO AL CAJERO AUTOMÁTICO ---")

# 2. Simulación de Validación de PIN (Bucle 'while' para seguridad)
while intentos > 0:
    pin_ingresado = input("Por favor, ingrese su PIN: ")

    if pin_ingresado == pin_correcto:
        print("\nPIN correcto. Acceso concedido.")
        break  # Sale del bucle de PIN
    else:
        intentos -= 1
        print(f"PIN incorrecto. Le quedan {intentos} intentos.")
        if intentos == 0:
            print("Tarjeta bloqueada. Demasiados intentos fallidos.")
            exit()  # Termina el programa

# 3. Menú Principal del Cajero (Bucle 'while' principal)
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    # 4. Estructura de Decisión (Condicionales if/elif/else)
    if opcion == '1':
        # --- CONSULTAR SALDO ---
        print(f"\nSu saldo actual es: ${saldo:.2f}")

    elif opcion == '2':
        # --- DEPOSITAR DINERO ---
        try:
            monto_deposito = float(input("Ingrese el monto a depositar: $"))
            if monto_deposito > 0:
                saldo += monto_deposito
                print(f"Depósito exitoso. Su nuevo saldo es: ${saldo:.2f}")
            else:
                print("⚠️ El monto del depósito debe ser positivo.")
        except ValueError:
            print("⛔ Entrada inválida. Por favor, ingrese un número.")

    elif opcion == '3':
        # --- RETIRAR DINERO ---
        try:
            monto_retiro = float(input("Ingrese el monto a retirar: $"))

            if monto_retiro <= 0:
                print("⚠️ El monto del retiro debe ser positivo.")
            elif monto_retiro > saldo:
                print("❌ Fondos insuficientes. No puede retirar esa cantidad.")
            else:
                saldo -= monto_retiro
                print(f"Retiro exitoso. Tome su dinero. Su nuevo saldo es: ${saldo:.2f}")

        except ValueError:
            print("⛔ Entrada inválida. Por favor, ingrese un número.")

    elif opcion == '4':
        # --- SALIR ---
        print("\nGracias por usar el Cajero Automático. ¡Vuelva pronto!")
        break  # Rompe el bucle 'while' principal, terminando el programa

    else:
        print("Opción no válida. Por favor, intente de nuevo.")