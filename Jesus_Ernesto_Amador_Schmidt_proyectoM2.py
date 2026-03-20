# Jesus_Ernesto_Amador_Schmidt_proyectoM2.py

# -----------------------------------
# RETO 1: Longitud de una palabra
# -----------------------------------

def analizar_palabra():
    while True:
        palabra = input("Ingresa una palabra: ").strip()

        # Validar que no esté vacía
        if palabra == "":
            print("Error: No puedes ingresar una cadena vacía.")
            continue

        longitud = len(palabra)

        if 4 <= longitud <= 8:
            print("La palabra es correcta.")
        elif longitud < 4:
            print(f"Hacen falta letras. Solo tiene {longitud} letras.")
        else:
            print(f"Sobran letras. Tiene {longitud} letras.")
        break


# -----------------------------------
# RETO 2: Cuadrante en el plano cartesiano
# -----------------------------------

def encontrar_cuadrante():
    try:
        x = float(input("Ingresa el valor de X: "))
        y = float(input("Ingresa el valor de Y: "))

        # Validación
        if x == 0 or y == 0:
            print("Error: Ninguna coordenada puede ser 0.")
            return

        if x > 0 and y > 0:
            print("El punto está en el Cuadrante I.")
        elif x < 0 and y > 0:
            print("El punto está en el Cuadrante II.")
        elif x < 0 and y < 0:
            print("El punto está en el Cuadrante III.")
        elif x > 0 and y < 0:
            print("El punto está en el Cuadrante IV.")

    except ValueError:
        print("Error: Debes ingresar números válidos.")


# -----------------------------------
# MENÚ PRINCIPAL
# -----------------------------------

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Analizar longitud de palabra")
        print("2. Encontrar cuadrante")
        print("3. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            analizar_palabra()
        elif opcion == "2":
            encontrar_cuadrante()
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida, intenta nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()