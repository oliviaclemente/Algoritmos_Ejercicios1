#Función más_frecuente(secuencia):
    #Diccionario conteo
    
    #Para cada número en secuencia:
        #Si el número está en conteo:
            #Incrementar su conteo en 1
        #Sino:
            #Añadir el número a conteo con un conteo inicial de 1
    
    #Mayor_frecuencia = 0
    #Número_más_frecuente = 0
    
    #Para cada número, frecuencia en conteo:
        #Si frecuencia > Mayor_frecuencia:
            #Mayor_frecuencia = frecuencia
            #Número_más_frecuente = número
    
    #Devolver Número_más_frecuente
    


    
def mas_frecuente(secuencia):
    # Diccionario para almacenar el conteo de cada número
    conteo = {}
    
    # Conteo de frecuencia de cada número en la secuencia
    for num in secuencia:
        if num in conteo:
            conteo[num] += 1
        else:
            conteo[num] = 1
    
    # Encontrar el número con la mayor frecuencia
    max_frecuencia = 0
    num_mas_frecuente = None
    for num, frecuencia in conteo.items():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            num_mas_frecuente = num
    
    return num_mas_frecuente

# Ejemplo de uso
secuencia = [1, 2, 3, 4, 2, 3, 1, 2, 4, 4, 4, 1, 1, 2, 3, 3, 3]
resultado = mas_frecuente(secuencia)
print("El número más frecuente es:", resultado)
