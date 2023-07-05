from listaClass import Lista
from colaClass import Cola
from pilaClass import Pila

class Personaje():

    def __init__(self, superheroe, nombre, grupo, grupo2, anioAparicion):
        self.superheroe = superheroe
        self.nombre = nombre
        self.grupo = grupo
        self.grupo2 = grupo2
        self.anioAparicion = anioAparicion
    def __str__(self):
        return f'{self.superheroe } - {self.nombre} - {self.grupo} - {self.grupo2} - {self.anioAparicion}'
    
p1 = Personaje('Vlack Widow', 'Natasha Romanoff', 'Avengers','', 1953)
p2 = Personaje('Captain America', 'Steve Rogers', 'Avengers', '', 1943)
p3 = Personaje('Iron Man', 'Tony Stark', 'Avengers', '', 1945)
p4 = Personaje('Hawkeye', 'Clint Barton', 'Avengers','', 1963)
p5 = Personaje('Spider-Man', ' Peter Parker', 'Avengers','', 1961)
p6 = Personaje('Capitana Marvel', 'Carol Danvers', 'Avengers','', 1960)
p7 = Personaje('Star-Lord', 'Peter Quill', 'Guardianes de la Galaxia','', 1978)
p8 = Personaje('Falcon', ' Sam Wilson', 'Avengers','', 1967)
p9 = Personaje('Black Panther', ' TChalla', 'Avengers','', 1954)
p10 = Personaje('Quicksilver', ' Pietro Maximoff', 'Avengers','', 1952)
p11 = Personaje('Ant-Man', ' Scott Lang', 'Avengers','', 1967)
p12 = Personaje('Man', ' Stark', 'Avengers','', 1969)
p13 = Personaje('Vision', ' Vision', 'Avengers','', 1989)
p14 = Personaje('War Machine ', ' James Rhodes ', 'Avengers','', 1986)
p15 = Personaje('Gamora  ', ' Gamora  ', 'Guardianes de la Galaxia','Los cuatro fantasticos', 1972)
p16 = Personaje('Thor', 'Thor Odinson', 'Avengers','', 1965)

personajes =[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16]

p_aux1 = Personaje('Nebula ', ' Nebula ', 'Guardianes de la Galaxia','Los cuatro fantasticos', 1990)
p_aux2 = Personaje('Rocket Raccoon ', ' Rocket ', 'Guardianes de la Galaxia','Los cuatro fantasticos', 1972)
p_aux3 = Personaje('Loki ', ' Loki ', 'Los cuatro fantasticos','', 1945)
p_aux4 = Personaje('Hulk ', ' Bruce Banner ', 'Avengers','', 1945)

personajes_aux = [p_aux1,p_aux2,p_aux3,p_aux4]
superheroes = Pila()
list_Personajes = Lista()
guardianesGalaxia = Cola()

for personaje in personajes:
    list_Personajes.insert(personaje,"superheroe")

#Punto F
for personaje in personajes_aux:
    list_Personajes.insert(personaje,"superheroe")

#Punto A
buscado = False
for i in range(0,list_Personajes.size()):
    if list_Personajes.get_element_by_index(i).superheroe == "Capitana Marvel":
        print(' Capitana Marvel se encuentra en la lista, y su nombre es: ', list_Personajes.get_element_by_index(i).nombre)
        buscado = True
if not buscado:
    print('Capitana Marvel no se encuentra en la lista')

#Punto B 
for i in range(0,list_Personajes.size()):
    if list_Personajes.get_element_by_index(i).grupo == "Guardianes de la Galaxia":
        guardianesGalaxia.arrive(list_Personajes.get_element_by_index(i))

print('Cantidad de superheroes que pertenezcan al grupo “Guardianes de la galaxia”: ',guardianesGalaxia.size())

#Punto C
for i in range(0,list_Personajes.size()):
    if list_Personajes.get_element_by_index(i).grupo == "Guardianes de la Galaxia" and list_Personajes.get_element_by_index(i).grupo2 == "Los cuatro fantasticos" :
        superheroes.push(list_Personajes.get_element_by_index(i))
print('Superheroes que pertenecen a los grupos "Guardianes de la Galaxia" y "Los Cuatro Fantasticos": ')
while superheroes.size() > 0:
    print(superheroes.pop())

#Punto D
print('Superheroes que cuyo año de aparición sea posterior a 1960: ')
for i in range(0,list_Personajes.size()):
    if list_Personajes.get_element_by_index(i).anioAparicion > 1960:
        print(list_Personajes.get_element_by_index(i).superheroe +', año '+str(list_Personajes.get_element_by_index(i).anioAparicion))

#Punto E
list_Personajes.set_value('Vlack Widow','Black Widow',"nombre")

#Punto G
print('Todos los personajes que comienzan con C, P o S: ')
for i in range(0,list_Personajes.size()):
    if list_Personajes.get_element_by_index(i).superheroe[0] in ['C','P','S']:
        print(list_Personajes.get_element_by_index(i).superheroe)

