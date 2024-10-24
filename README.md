# Transformación y Análisis de Gramáticas Libres de Contexto

Este proyecto implementa una serie de algoritmos para transformar una gramática libre de contexto, eliminando la recursión por la izquierda, realizando la factorización y calculando los conjuntos FIRST y FOLLOW, así como la tabla de producción para la gramática.

## Contenido

- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Algoritmos Implementados](#algoritmos-implementados)
- [Ejemplo de Ejecución](#ejemplo-de-ejecución)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción

El objetivo de este proyecto es facilitar la transformación y el análisis de gramáticas libres de contexto para su uso en la construcción de analizadores sintácticos. Los principales pasos incluyen:

1. **Eliminación de recursión por la izquierda:** Para evitar bucles infinitos en el análisis.
2. **Factorización de la gramática:** Para eliminar ambigüedades y facilitar la construcción de analizadores predictivos.
3. **Cálculo de los conjuntos FIRST y FOLLOW:** Elementos fundamentales para la construcción de la tabla de análisis sintáctico.
4. **Construcción de la tabla de producción:** Utilizada en analizadores sintácticos predictivos.

## Requisitos

- Python 3.x

## Instalación

1. Descarga este repositorio:
   

Uso

    Ejecuta el archivo gramatica.py:

    bash

    python gramatica.py

    Esto generará la salida en la consola, mostrando las transformaciones de la gramática y los cálculos de FIRST, FOLLOW y la tabla de producción.

Algoritmos Implementados
1. Eliminación de Recursión por la Izquierda

El algoritmo identifica producciones recursivas por la izquierda y las elimina creando nuevas producciones, con nuevos no terminales si es necesario.
2. Factorización de la Gramática

Agrupa producciones con prefijos comunes y las factoriza para eliminar ambigüedades.
3. Cálculo del Conjunto FIRST

El conjunto FIRST contiene todos los símbolos terminales que pueden aparecer al principio de cualquier cadena derivada de un no terminal.
4. Cálculo del Conjunto FOLLOW

El conjunto FOLLOW contiene todos los símbolos que pueden seguir a un no terminal en cualquier derivación.
5. Construcción de la Tabla de Producción

La tabla de producción mapea pares (no_terminal, terminal) con la producción correspondiente, lo cual es esencial para analizadores sintácticos predictivos.
Ejemplo de Ejecución

Dada la siguiente gramática:

python

gramatica_inicial = {
    "S": ["Aa", "b"],
    "A": ["Ac", "Sd", "ε"]
}

El programa realizará los siguientes pasos:

    Eliminación de la recursión por la izquierda:

    plaintext

Gramática sin recursión izquierda: {'S': ['Aa', 'b'], 'A': ['Sd', 'Ac', 'ε']}

Factorización de la gramática:

plaintext

Gramática factorizada: {'S': ['Aa', 'b'], 'A': ['A_factd', 'A_factc', 'ε']}

Cálculo del conjunto FIRST:

plaintext

Conjunto FIRST: {'S': {'b', 'A'}, 'A': {'d', 'c', 'ε'}}

Cálculo del conjunto FOLLOW:

plaintext

Conjunto FOLLOW: {'S': {'$'}, 'A': {'d', 'c', 'ε'}}

Construcción de la Tabla de Producción:

plaintext

Tabla de Producción: {('S', 'a'): 'Aa', ('A', 'c'): 'cA\'', ('A', 'd'): 'dA\''}
