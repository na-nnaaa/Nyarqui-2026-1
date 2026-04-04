
# Integrantes
- Iker Ortiz - 202473562-4 - Paralelo 201
- Gabriel Ordenes - 202473521-7 - Paralelo 201

# Especificación de los algoritmos y desarrollo realizado:

Para resolver este laboratorio, dividimos el problema en dos partes principales: la lectura/filtrado del archivo y la conversión matemática pura entre las distintas bases.

1. Lectura de archivo y filtrado de ruido
-Para procesar el archivo `notas_dm.txt`, decidimos leerlo caracter por caracter (`arch.read(1)`). Esto nos pareció mucho más seguro y eficiente que cargar todo de golpe, ya que nos permite ir evaluando el "ruido" en tiempo real. 
-Implementamos una lógica basada en un "acumulador". El programa va revisando los caracteres y cuando detecta uno de los prefijos válidos (*, &, #, !), activa una variable de estado (`base_actual`) y empieza a guardar los números que vienen después. Para saber cuándo termina el número y empieza el ruido (o el siguiente número), creamos la función `es_digito_valido`. Si el caracter que leemos no pertenece a la base actual (por ejemplo, una 'A' cuando estamos leyendo en base 8), el programa asume que el número terminó, lo manda a procesar, limpia el acumulador y sigue buscando el próximo prefijo.

2. Lógica de conversiones
Teníamos clarísimo que el uso de funciones como `bin()`, `oct()` o `int()` (en uno de sus usos) estaba prohibido, así que todas las conversiones se hicieron a mano, programando la matemática detrás de cada una para tener las 12 combinaciones posibles de forma directa.

- Hacia base Decimal: Ocupamos el sistema posicional clásico. Iteramos sobre el string numérico de derecha a izquierda, multiplicando cada dígito por la base original elevada a la posición correspondiente, y sumando todo.
- Desde base Decimal a otras bases: Implementamos el algoritmo de divisiones sucesivas. Dividimos el entero por la base de destino (2, 8 o 16) usando división entera (`//`), y vamos guardando el resto (`%`). Luego, damos vuelta el string resultante. En el caso de hexadecimal, hicimos un mapeo manual para que los restos del 10 al 15 se transformen en letras de la 'A' a la 'F'.
- Conversiones entre potencias de 2 (Binario, Octal y Hexadecimal): Para no usar el decimal como puente y hacer la conversión directa, aprovechamos que estas bases son proporcionales. Para pasar de binario a octal, agrupamos los bits de a 3 de derecha a izquierda y los reemplazamos por su equivalente. Para binario a hexadecimal, los agrupamos de a 4. Las conversiones inversas funcionan de la misma forma, reemplazando un dígito octal o hexa por su bloque directo de 3 o 4 ceros y unos.

Para el filtrado final del mensaje, cualquier número que al pasarlo a decimal nos diera menor a 32 o mayor a 126, simplemente no se agrega al string del mensaje final ASCII ni se imprime en la lista de valores encontrados.


# Supuestos utilizados

Durante el desarrollo del código, tomamos las siguientes decisiones y supuestos:

1. Formato de las letras Hexadecimales: Asumimos que los caracteres válidos para el sistema hexadecimal vienen en mayúsculas dentro del archivo de texto (A, B, C, D, E, F). Si vienen en minúscula, nuestra función `es_digito_valido` los considerará como ruido y cortará la captura del número en ese punto.
2. Definición del límite del ruido: Asumimos que el "ruido" también actúa como un separador natural. Si el archivo dice `#145xyz`, el programa asume que el número decimal válido es solo "145", lo procesa, y descarta el "xyz" silenciosamente hasta que encuentre otro símbolo de inicio (*, &, #, !).
3. Rango inclusivo: El enunciado menciona "entre el rango 32 y 126", por lo que asumimos que los bordes son inclusivos (es decir, el 32 y el 126 sí cuentan y se transforman a ASCII).
4. El archivo existe en la misma ruta: Asumimos que el archivo `notas_dm.txt` estará ubicado en la misma carpeta desde donde se ejecute el script de Python. De todas formas, pusimos un bloque `try-except` para que no se caiga feo si no lo encuentra y avise por consola.
5. Archivos sin saltos de línea al final: Asumimos que el número cifrado puede estar pegado justo al final del archivo. Por eso, al detectar el fin del archivo (`if not caracter:`), pusimos un chequeo extra para procesar cualquier número que haya quedado en el acumulador antes de que se acabara el texto.