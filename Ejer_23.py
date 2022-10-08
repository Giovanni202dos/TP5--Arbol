"""
Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
resuelva las siguientes consultas:
a. listado inorden de las criaturas y quienes la derrotaron;
b. se debe permitir cargar una breve descripción sobre cada criatura;
c. mostrar toda la información de la criatura Talos;
d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
o dios que la capturo;
h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
Erimanto indicando que Heracles las atrapó;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;
k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles.
"""
from arbol import *

arbol= nodoArbol()

insertar_nodo(arbol, 'Ceto',{'derrotado por':'-'})
insertar_nodo(arbol, 'Tifón',{'derrotado por':'Zeus'})
insertar_nodo(arbol, 'Equidna',{'derrotado por':'Argos Panoptes'})
insertar_nodo(arbol, 'Dino',{'derrotado por':'-'})
insertar_nodo(arbol, 'Pefredo',{'derrotado por':'-'})
insertar_nodo(arbol, 'Enio',{'derrotado por':'-'})
insertar_nodo(arbol, 'Escila',{'derrotado por':'-'})
insertar_nodo(arbol, 'Caribdis',{'derrotado por':'-'})
insertar_nodo(arbol, 'Euríale',{'derrotado por':'-'})
insertar_nodo(arbol, 'Esteno',{'derrotado por':'-'})
insertar_nodo(arbol, 'Medusa',{'derrotado por':'Perseo'})
insertar_nodo(arbol, 'Ladón',{'derrotado por':'Heracles'})
insertar_nodo(arbol, 'Águila del Cáucaso',{'derrotado por':'-'})
insertar_nodo(arbol, 'Quimera',{'derrotado por':'Belerofonte'})
insertar_nodo(arbol, 'Hidra de Lerna',{'derrotado por':'Heracles'})
insertar_nodo(arbol, 'León de Nemea',{'derrotado por':'Heracles'})
insertar_nodo(arbol, 'Esfinge',{'derrotado por':'Edipo'})
insertar_nodo(arbol, 'Dragón de la Cólquida',{'derrotado por':'-'})
insertar_nodo(arbol, 'Cerbero',{'derrotado por':'-'})

insertar_nodo(arbol, 'Cerda de Cromión',{'derrotado por':'Teseo'})
insertar_nodo(arbol, 'Ortro',{'derrotado por':'Heracles'})
insertar_nodo(arbol, 'Toro de Creta',{'derrotado por':'Teseo'})
insertar_nodo(arbol, 'Jabalí de Calidón',{'derrotado por':'Atalanta'})
insertar_nodo(arbol, 'Carcinos',{'derrotado por':'-'})
insertar_nodo(arbol, 'Gerión',{'derrotado por':'Heracles'})
insertar_nodo(arbol, 'Cloto',{'derrotado por':'-'})
insertar_nodo(arbol, 'Láquesis',{'derrotado por':'-'})
insertar_nodo(arbol, 'Átropos',{'derrotado por':'-'})
insertar_nodo(arbol, 'Minotauro de Creta',{'derrotado por':'Teseo'})
insertar_nodo(arbol, 'Harpías',{'derrotado por':'-'})
insertar_nodo(arbol, 'Argos Panoptes',{'derrotado por':'Hermes'})
insertar_nodo(arbol, 'Aves del Estínfalo',{'derrotado por':'-'})
insertar_nodo(arbol, 'Talos',{'derrotado por':'Medea'})
insertar_nodo(arbol, 'Sirenas',{'derrotado por':'-'})
insertar_nodo(arbol, 'Pitón',{'derrotado por':'Apolo'})
insertar_nodo(arbol, 'Cierva de Cerinea',{'derrotado por':'-'})
insertar_nodo(arbol, 'Basilisco',{'derrotado por':'-'})
insertar_nodo(arbol, 'Jabalí de Erimanto',{'derrotado por':'-'})


#a
print()
print('a:')
print('listado inorden de las criaturas y quienes la derrotaron: ')
inorden_criaturas(arbol)

#b
print()
print('b:')
print('se debe permitir cargar una breve descripción sobre cada criatura: ')
print('criatura que tienen una breve descricpcion: ')
cargar_breve_descripcion_a_criatura_x(arbol,'Talos','muuy malo')
cargar_breve_descripcion_a_criatura_x(arbol,'Jabalí de Erimanto','grande')
cargar_breve_descripcion_a_criatura_x(arbol,'Harpías','muuy feroz')
cargar_breve_descripcion_a_criatura_x(arbol,'Átropos','nada')
cargar_breve_descripcion_a_criatura_x(arbol,'Láquesis','inteligente')
cargar_breve_descripcion_a_criatura_x(arbol,'Ceto','voraz')
cargar_breve_descripcion_a_criatura_x(arbol,'Dino','blabla')
cargar_breve_descripcion_a_criatura_x(arbol,'Cerbero','voraz')
cargar_breve_descripcion_a_criatura_x(arbol,'Basilisco','malo')
criaturas_con_breve_descripcion(arbol)

#c
print()
print('c:')
print('mostrar toda la información de la criatura Talos: ')
mostrar_criatura_x(arbol,'Talos')

#d         
#PARA LOGRAR ESTO UTILICE UN OBJETO DIOS(q guarda el nombre y la cantidad de criaturas q derroto) Y UNA LISTA LA CUAL GUARDA 
#OBJETOS DE TIPO DIOS Y LO GUARDE CON EL CRITERIO DE ORDEN  DE QUIEN MATO MAS CRIATURAS, LUEGO PARA DAR A CONOCER
#QUIEN ES EL Q MAS TIENE CRIATURAS DERROTADAS LO FUI MOSTRANDO E ELIMINANDO DE LA LISTA
print()
print('d:')
print('determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas: ')
lista_de_dioses=Lista()
pasar_dioses_a_lista_para_averiguar_mayor_captura_de_criaturas(arbol,lista_de_dioses)
print('en primer lugar esta: ')
dios = mostrar_dios_con_mayor_criaturas_derrotadas_de_la_lista(lista_de_dioses)
print(dios.nombre, ' con: ', dios.canti_de_criaturas_derrotadas)
lista_de_dioses.eliminar(dios.nombre,'nombre')  #lo eliminamos(para asi si quieres buscar otro q sea mayor)

print('en segundo lugar esta: ')
dios = mostrar_dios_con_mayor_criaturas_derrotadas_de_la_lista(lista_de_dioses)
print(dios.nombre, ' con: ', dios.canti_de_criaturas_derrotadas)
lista_de_dioses.eliminar(dios.nombre,'nombre')  #lo eliminamos(para asi si quieres buscar otro q sea mayor) 

print('en tercer lugar esta: ')
dios = mostrar_dios_con_mayor_criaturas_derrotadas_de_la_lista(lista_de_dioses)
print(dios.nombre, ' con: ', dios.canti_de_criaturas_derrotadas)
lista_de_dioses.eliminar(dios.nombre,'nombre')  #lo eliminamos(para asi si quieres buscar otro q sea mayor) 
#lista_de_dioses.barrido()

#e
print()
print('e: listar las criaturas derrotadas por Heracles: ')
mostrar_todas_las_criaturas_derrotada_por_dios_x(arbol, 'Heracles')

#f
print()
print('f: listar las criaturas que no han sido derrotadas (osea q tengan un - )')
mostrar_todas_las_criaturas_q_no_fueron_derrotadas(arbol)

#g      
print()
print('g:además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo (sera lo mismo q derrotada por? o q? yo le agregue un nuevo campo "capturado" en el cual le copie lo q esta en derrotada por )')
agregar_campo_capturadas_a_todas_las_criaturas(arbol)
inorden_criaturas(arbol)

#h  
print()
print('h:modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó')
modificar_el_campo_capturada_de_x_criatura(arbol, 'Cerbero','Heracles')
modificar_el_campo_capturada_de_x_criatura(arbol, 'Toro de Creta','Heracles')
modificar_el_campo_capturada_de_x_criatura(arbol, 'Cierva de Cerinea','Heracles')
modificar_el_campo_capturada_de_x_criatura(arbol, 'Jabalí de Erimanto','Heracles')

mostrar_criatura_x(arbol,'Cerbero')
mostrar_criatura_x(arbol,'Toro de Creta')
mostrar_criatura_x(arbol,'Cierva de Cerinea')
mostrar_criatura_x(arbol,'Jabalí de Erimanto')
#inorden_criaturas(arbol)

#i   
print()
print('i: se debe permitir búsquedas por coincidencia (q con solo introducir una palbra hay q mostrar las criaturas q tengan ese dato relacionado)')
busqueda_por_coincidencia(arbol,'heracles')

#j
print()
print('j: eliminar al Basilisco y a las Sirenas;')
eliminar_nodo(arbol, 'Basilisco')
eliminar_nodo(arbol, 'Sirenas')
inorden_criaturas(arbol)

#k
print()
print("k: modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;")
modificar_el_campo_derrotado_de_x_criatura(arbol,'Aves del Estínfalo','Heracles')
mostrar_criatura_x(arbol,'Aves del Estínfalo')

#l  #como el arbol esta ordenado por el campo info(q seria el nombre de la criatura) tendremos q eliminar el nodo e insertarlo de nuevo con el nuevo nombre
print()
print('l: modifique el nombre de la criatura Ladón por Dragón Ladón;')
modificar_el_campo_info_de_x_criatura(arbol,'Ladón' ,'Dragón Ladón')
inorden_criaturas(arbol)

#m
print()
print('m: realizar un listado por nivel del árbol;')
por_nivel(arbol)

#n
print()
print('n: muestre las criaturas capturadas por Heracles.')
mostrar_todas_las_criaturas_q_fueron_capturada_por_x_dios(arbol,'Heracles')

