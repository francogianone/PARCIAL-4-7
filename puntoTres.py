from pilaClass import Pila

stack = Pila()
planeta1 = {"planeta": "Bespin", "capturado": "Lando Calrissian", "recompensa": 33000}
planeta2 = {"planeta": "Endor", "capturado": "nadie", "recompensa": 14500}
planeta3 = {"planeta": "Tatooine", "capturado": "Han Solo", "recompensa": 87000}
planetas = [planeta1,planeta2,planeta3]

bitacora = Pila()
bitacora_aux = Pila()
cont_Mision = 0
misionBuscada = 0
creditosGalacticos = 0

for mision in planetas:
    bitacora.push(mision)
while bitacora.size() > 0:
    value = bitacora.pop()
    bitacora_aux.push(value)
    creditosGalacticos += value["recompensa"]

#Punto A
print('Planetas visitados en el orden hizo las misiones:')
while bitacora_aux.size() > 0:
    value = bitacora_aux.pop()
    print(value["planeta"])
    cont_Mision += 1
    if value["capturado"] == "Han Solo":
        misionBuscada = cont_Mision

#Punto B
print(f'Total de creditos galacticos recaudados: {creditosGalacticos}')

#Punto C
print(f'Han Solo fue capturado en la mision { misionBuscada } en el planeta {planetas[misionBuscada - 1][ "planeta" ]}')

