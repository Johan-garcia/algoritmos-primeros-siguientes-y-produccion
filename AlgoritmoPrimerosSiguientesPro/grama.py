#GRAMÁTICA:

# Representación de la gramática original
gramatica_inicial = {
    "S": ["ABC", "S"],
    "A": ["BCD", "A", "ε"],
    "B": ["DC", "ε"],
    "C": ["DB", "ε"],
    "D": ["ε"]
}

#algoritmos de transformación
print(f"gramatica_sin_transformacion: {gramatica_inicial}")

#ELIMINACIÓN DE RECURSIÓN POR LA IZQUIERDA
def eliminar_recursion_izquierda(gramatica):
    nueva_gramatica = {}
    for no_terminal, producciones in gramatica.items():
        recursivas = []
        no_recursivas = []

        # Separar las producciones recursivas y no recursivas
        for prod in producciones:
            if prod.startswith(no_terminal):
                recursivas.append(prod[len(no_terminal):])  # Quitar el no_terminal recursivo
            else:
                no_recursivas.append(prod)

        # Si no hay recursión, agregar tal cual
        if not recursivas:
            nueva_gramatica[no_terminal] = producciones
        else:
            # Crear un nuevo no terminal para eliminar la recursión
            nuevo_no_terminal = no_terminal + "'"
            nueva_gramatica[no_terminal] = [nr + nuevo_no_terminal for nr in no_recursivas]
            nueva_gramatica[nuevo_no_terminal] = [r + nuevo_no_terminal for r in recursivas] + ["ε"]

    return nueva_gramatica

# Transformación de la gramática
gramatica_sin_recursion = eliminar_recursion_izquierda(gramatica_inicial)
print("Gramática sin recursión izquierda:", gramatica_sin_recursion)



#FACTORIZACIÓN DE LA GRAMÁTICA

from collections import defaultdict

def factorizar_gramatica(gramatica):
    nueva_gramatica = {}
    for no_terminal, producciones in gramatica.items():
        prefijos_comunes = defaultdict(list)

# Agrupar producciones por prefijo común
        for prod in producciones:
            if len(prod) > 0:
                prefijo = prod[0]
                prefijos_comunes[prefijo].append(prod)

# Reconstruir las producciones
        nuevas_producciones = []
        for prefijo, grupo in prefijos_comunes.items():
            if len(grupo) == 1:
                nuevas_producciones.append(grupo[0])
            else:
                nuevo_no_terminal = no_terminal + "_fact"
                nuevas_producciones.append(prefijo + nuevo_no_terminal)
                nueva_gramatica[nuevo_no_terminal] = [p[1:] if len(p) > 1 else "ε" for p in grupo]

        nueva_gramatica[no_terminal] = nuevas_producciones

    return nueva_gramatica

# Factorización de la gramática
gramatica_factorizada = factorizar_gramatica(gramatica_sin_recursion)
print("Gramática factorizada:", gramatica_factorizada)



#FACTORIZACIÓN DE LA GRAMÁTICA

from collections import defaultdict

def factorizar_gramatica(gramatica):
    nueva_gramatica = {}
    for no_terminal, producciones in gramatica.items():
        prefijos_comunes = defaultdict(list)

        # Agrupar producciones por prefijo común
        for prod in producciones:
            if len(prod) > 0:
                prefijo = prod[0]
                prefijos_comunes[prefijo].append(prod)

        # Reconstruir las producciones
        nuevas_producciones = []
        for prefijo, grupo in prefijos_comunes.items():
            if len(grupo) == 1:
                nuevas_producciones.append(grupo[0])
            else:
                nuevo_no_terminal = no_terminal + "_fact"
                nuevas_producciones.append(prefijo + nuevo_no_terminal)
                nueva_gramatica[nuevo_no_terminal] = [p[1:] if len(p) > 1 else "ε" for p in grupo]

        nueva_gramatica[no_terminal] = nuevas_producciones

    return nueva_gramatica

# Factorización de la gramática
gramatica_factorizada = factorizar_gramatica(gramatica_sin_recursion)
print("Gramática factorizada:", gramatica_factorizada)
