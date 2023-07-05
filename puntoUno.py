v_palabras = ["auto", "auto", "camioneta", "avion", "auto"]

def contar_palabra(vector, palabra):
    if not vector:  
        return 0
    elif vector[0] == palabra:  
        return 1 + contar_palabra(vector[1:], palabra)  
    else:  
        return contar_palabra(vector[1:], palabra)  

buscar = str(input('Ingrese palabra a buscar:'))
resultado = contar_palabra(v_palabras, buscar)
print(f"'{buscar}' aparece {resultado} veces en el vector.")
