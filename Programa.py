# Nueva matriz de transición del AFD.
transiciones_nueva = {
    'A': {'a': 'B', 'b': None, 'c': None, 'd': None},
    'B': {'a': None, 'b': 'C', 'c': 'C', 'd': None},
    'C': {'a': None, 'b': 'C', 'c': 'C', 'd': 'D'},
    'D': {'a': None, 'b': None, 'c': None, 'd': None}
}

# Asumir que 'A' es el estado inicial y 'D' es un estado de aceptación.
estado_inicial_nuevo = 'A'
estados_aceptacion_nuevo = {'D'}

# Función que verifica si una cadena es aceptada por el nuevo AFD.
def acepta_cadena_nueva(cadena, estado_inicial, transiciones, estados_aceptacion):
    estado_actual = estado_inicial
    
    for simbolo in cadena:
        if simbolo in transiciones[estado_actual] and transiciones[estado_actual][simbolo] is not None:
            estado_actual = transiciones[estado_actual][simbolo]
        else:
            return False
    return estado_actual in estados_aceptacion

# Bucle que permite al usuario verificar cadenas repetidamente hasta que decida salir.
while True:
    print("---------------------------------------------")
    print("REALIZADO POR:\n Juan Carrillo\n Daniel Escorcia\n David Silvera ")
    print("---------------------------------------------")
    print("\n1. Ingresar y verificar una cadena.")
    print("2. Salir.")
    opcion = input("Elige una opción: ")
    print("---------------------------------------------")

    if opcion == '1':
        cadena_ingresada_por_usuario = input("Por favor, ingresa la cadena que deseas verificar: ")
        resultado_nuevo = acepta_cadena_nueva(cadena_ingresada_por_usuario, estado_inicial_nuevo, transiciones_nueva, estados_aceptacion_nuevo)
        print("---------------------------------------------")
        print("La cadena '{}' es {}.".format(cadena_ingresada_por_usuario, "aceptada" if resultado_nuevo else "rechazada"))
    elif opcion == '2':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
