Laboratorio N2 INF245

Integrantes:
Iker Ortiz | 202473562-4 P201
Gabriel Ordenes | 202473521-7 P201

Seccion 1: Análisis teórico (Tablas de verdad y Karnaugh)

Especificación de los algoritmos y desarrollo realizado:

-Construcción de la Tabla de Verdad: A partir de la "Tabla rúnica" entregada en el enunciado, se elaboró una tabla de verdad completa. Se mapearon las 16 combinaciones posibles de entrada (los 4 bits) hacia los 7 segmentos individuales del display (a, b, c, d, e, f, g), asignando estados lógicos correspondientes para cada caso.
-Simplificación mediante Mapas de Karnaugh: Se construyeron 7 mapas de Karnaugh (uno por cada segmento de salida). El proceso consistió en traspasar los "1" lógicos de la tabla de verdad a las grillas ordenadas bajo el código Gray.
    *Agrupación y obtención de funciones: Se procedió a encerrar los "1" en grupos de potencias de 2 (priorizando grupos de 4 celdas y luego de 2). Se aprovechó la adyacencia de los bordes del mapa para maximizar el tamaño de los grupos. Finalmente, descartando las variables que cambiaban de estado dentro de cada grupo, se extrajeron las 7 ecuaciones booleanas minimizadas.

Supuestos utilizados

Durante esta fase de modelado teórico, se asumieron las siguientes consideraciones:

-Orden de los Bits: Para las entradas "A3, A2, A1, A0", se utilizaron los nombres "D, C, B, A" respectivamente. Se asume que A3 (al que llamamos D en nuestro desarrollo) es el bit más significativo (MSB) y A0 (al que llamamos A) es el bit menos significativo (LSB).
-Ordenamiento de los Mapas: Se asume como estándar el uso del código Gray (00, 01, 11, 10) para las coordenadas de filas y columnas en los mapas de Karnaugh, garantizando así que la adyacencia visual en el mapa corresponda a la adyacencia lógica real para la simplificación.
-Orden de filas y columnas: Para los mapas de Karnaugh, se utiliza DC en las filas (de arriba hacia abajo) y BA en las columnas (de izquierda a derecha).