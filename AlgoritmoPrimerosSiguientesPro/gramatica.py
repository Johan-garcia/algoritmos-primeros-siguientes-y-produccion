#GRAMÁTICA:

# Representación de la gramática original
gramatica_inicial = {
    "S": ["Aa", "b"],
    "A": ["Ac", "Sd", "ε"]
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

# Algoritmo para calcular el conjunto FIRST
def calcular_first(gramatica):
    first = {nt: set() for nt in gramatica}

    # Repetir hasta que no haya cambios
    cambio = True
    while cambio:
        cambio = False
        for nt in gramatica:
            for prod in gramatica[nt]:
                if len(prod) == 0 or prod == "ε":
                    # Si la producción es ε, añadir ε a FIRST
                    if "ε" not in first[nt]:
                        first[nt].add("ε")
                        cambio = True
                else:
                    for simbolo in prod:
                        # Añadir FIRST del símbolo al FIRST del no terminal actual
                        if simbolo.islower() or simbolo == "ε":  # Es terminal o ε
                            if simbolo not in first[nt]:
                                first[nt].add(simbolo)
                                cambio = True
                            break
                        else:  # Es un no terminal
                            tamano_inicial = len(first[nt])
                            first[nt].update(first[simbolo] - {"ε"})
                            if "ε" not in first[simbolo]:
                                break
                            if len(first[nt]) > tamano_inicial:
                                cambio = True
                    else:
                        # Si todos los símbolos pueden derivar ε, añadir ε a FIRST
                        if "ε" not in first[nt]:
                            first[nt].add("ε")
                            cambio = True
    return first

# Algoritmo para calcular el conjunto FOLLOW
def calcular_follow(gramatica, first):
    follow = {nt: set() for nt in gramatica}
    follow["S"].add("$")  # Añadir el símbolo de fin de cadena al FOLLOW del símbolo inicial

    cambio = True
    while cambio:
        cambio = False
        for nt in gramatica:
            for prod in gramatica[nt]:
                trailer = follow[nt].copy()
                for simbolo in reversed(prod):
                    if simbolo.isupper():  # Es un no terminal
                        if not trailer.issubset(follow[simbolo]):
                            follow[simbolo].update(trailer)
                            cambio = True
                        if "ε" in first[simbolo]:
                            trailer.update(first[simbolo] - {"ε"})
                        else:
                            trailer = first[simbolo]
                    else:
                        trailer = {simbolo}
    return follow

# Algoritmo para calcular la tabla de producción
def calcular_produccion(gramatica, first, follow):
    produccion_tabla = {}

    for nt in gramatica:
        for prod in gramatica[nt]:
            # Calcular el conjunto de símbolos para la entrada actual
            conjunto_entrada = set()
            if prod[0].islower() or prod[0] == "ε":  # Comienza con un terminal o es ε
                conjunto_entrada.add(prod[0])
            else:  # Comienza con un no terminal
                conjunto_entrada.update(first[prod[0]])

                # Si ε está en el FIRST del primer símbolo, agregar FOLLOW del no terminal
                if "ε" in first[prod[0]]:
                    conjunto_entrada.remove("ε")
                    conjunto_entrada.update(follow[nt])

            # Asignar la producción correspondiente para cada símbolo en conjunto_entrada
            for simbolo in conjunto_entrada:
                produccion_tabla[(nt, simbolo)] = prod

    return produccion_tabla


# Calcular FIRST, FOLLOW y la tabla de producción para la gramática inicial
first = calcular_first(gramatica_factorizada)
follow = calcular_follow(gramatica_factorizada, first)
produccion_tabla = calcular_produccion(gramatica_factorizada, first, follow)

print("Conjunto FIRST:", first)
print("Conjunto FOLLOW:", follow)
print("Tabla de Producción:", produccion_tabla)
