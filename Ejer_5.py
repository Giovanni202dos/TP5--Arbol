"""
Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:
    I. determinar cuántos nodos tiene cada árbol;
    II. realizar un barrido ordenado alfabéticamente de cada árbol.
"""
from arbol import *

arbol = nodoArbol()
arbol_heroes = nodoArbol()
arbol_villanos = nodoArbol()
insertar_nodo(arbol,"ivan Vanko",False)
insertar_nodo(arbol,"batman",True)
insertar_nodo(arbol,"superman",True)
insertar_nodo(arbol,"capitan america",True)
insertar_nodo(arbol,"thor",True)
#insertar_nodo(arbol,"bbatman",True)
insertar_nodo(arbol,"thanos",False)
insertar_nodo(arbol,"calabera roja",False)
insertar_nodo(arbol,"tGanos",False)
insertar_nodo(arbol,"general Ross",False)



#print(arbol)
#a:
print("")
print("a:")
por_nivel(arbol)

#b;
print("")
print("b:")
print("listar los villanos alfabeticamente: ")
mostrar_alfabeticamente_los_villanos(arbol)

#c;
print("")
print("c:")
print("mostrar todos los superhéroes que empiezan con una letra x: ")
mostrar_todos_los_perosonajes_que_empiezan_con_letra_x(arbol,"t")

#d;
print("")
print("d:")
print("determinar cuántos superhéroes hay en el árbol:")
print(cantidad_de_elementos_personajes_guardados(arbol))

#e;
print("")
print("e:")
print("un perosonaje esta mal cargado.Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre")
#datos es el true o false (heroe o villano)para modificar un personaje lo tengo q eliminar y agregarlo de nuevo  es igual a una lista
nombre, datos=(eliminar_personaje(arbol,"thanos"))
nuevo_nombre = "bbatman malo"
insertar_nodo(arbol, nuevo_nombre, datos)

#f;
print("")
print("f:")
print("listar los superhéroes ordenados de manera descendente (es decir empezando desde la z)")
mostrar_todos_los_personajes_en_manera_descendente(arbol)

#g;
print("")
print("g:")
print("generar un bosque;un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:")
generar_bosque_de_villanos_y_heroes(arbol, arbol_heroes, arbol_villanos)
print("arbol de heroes:")
por_nivel(arbol_heroes)
print("")
print("arbol de villanos:")
por_nivel(arbol_villanos)

print("")
print("  g_1:")
print("  I. determinar cuántos nodos tiene el arbol de heroes y villanos;")
print("  cantidad de nodos del arbol de heroes: ",cantidad_de_elementos_personajes_guardados(arbol_heroes))
print("  cantidad de nodos del arbol de villanos: ",cantidad_de_elementos_personajes_guardados(arbol_villanos))

print("")
print("  g_2:")
print("  II. realizar un barrido ordenado alfabéticamente de cada árbol.:")
print("  arbol de heroes alfabeticamente: ")
mostrar_alfabeticamente_todos_los_personajes(arbol_heroes)
print("")
print("  arbol de villanos alfabeticamente: ")
mostrar_alfabeticamente_todos_los_personajes(arbol_villanos)
