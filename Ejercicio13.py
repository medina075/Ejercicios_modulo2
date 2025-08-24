def juego_aventura():
    print("Intenta escapar de la casa")
    print("Inicias en la sala de una casa de la que intentas escapar")
    print("Tu objetivo es encontrar la forma de salir.\n")

    habitacion = "sala"
    jugando = True

    while jugando:
        if habitacion == "sala":
            print("Te encuentras en la sala que camino eliges para intentar salir:")
            print(" 1 Ir al 'norte' hacia el garaje")
            print(" 2 Ir al 'este' hacia la puerta principal")
            accion = input("¿Qué haces? ").lower()

            if accion == "1":
                habitacion = "garaje"
            elif accion == "2":
                habitacion = "puerta"
            else:
                print("⚠️ Opción no válida.")

        elif habitacion == "garaje":
            print("\nHas entrado al garaje...")
            print("Hay un llavero con unas llaves en una mesa. Puedes:")
            print(" 1 'intentar prender el carro'")
            print(" 2 'intentar abrir la puerta principal'")
            accion = input("¿Qué haces? ").lower()

            if accion == "1":
                print("\nsubes al carro...")
                print("intentas encender el carro...")
                print("te escuchan intentar prenderlo...")
                print("logras encender el carro a tiempo...")
                print("atraviesas la puerta del garaje con el carro...")
                print("\n🎉 ¡Has escapado! ¡Ganaste!")
                jugando = False
            elif accion == "2":
                habitacion = "puerta"
            else:
                print("⚠️ Opción no válida.")

        elif habitacion == "puerta":
            print("\n⚔️ llegaste a la puerta...")
            print("la puerta esta cerrada con llave.")
            print("intentas forzar la puerta...")
            print("haces mucho ruido te descubren y te disparan. ¡Has perdido!")
            print("vuelve a iniciar el juego\n")
            habitacion="sala"


if __name__ == "__main__":
    juego_aventura()
