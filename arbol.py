from cola import Cola
from lista import Lista

def nodoArbol():
    nodo = {
        'info': None,   #aca se guarda la informacion
        'datos': None,  #aun nose porque esta esto
        'der': None,    #el hijo derecho
        'izq': None,    #el hijo izquierdo
        'altura': 0,
    }   #nodo es un diccionario clave:valor
    return nodo #retorno el nodo porque sino no se podra modificar el mismo

#no creo directamente izq y der un nodo porque quizas se haga un bucle
#por eso lo creo cuanto lo inserto

def copiar_nodo(nodo_datos, nodo_copia):
    if nodo_datos:
        nodo_copia['info'] = nodo_datos['info']
        nodo_copia['der'] = nodo_datos['der']
        nodo_copia['izq'] = nodo_datos['izq']
        if 'datos' in nodo_datos:
            nodo_copia['datos'] = nodo_datos['datos']


def insertar_nodo(arbol, dato, datos=None): #cada nodo es un arbol
    if arbol['info'] is None:               #si esta vacio info lo guarda ahi || arbol['info'] es igual a arbol.get("info") devuelve el valor
        arbol['info'] = dato
        arbol['datos'] = datos

    elif dato < arbol['info']:                  #sino, si el numero es menor se guarda en la izquierda
        if arbol['izq'] is None:                #tiene q comprobar si esta vacio
            arbol['izq'] = nodoArbol()              #si esta vacio entonces se crea un nodo alli mismo (osea otro diccionario)
        insertar_nodo(arbol['izq'], dato, datos)    #y se llama denuevo a la funcion y se guarda el dato
    else:                                           #si son iguales se lo guarda a la der
        if arbol['der'] is None:                #loo mismo q el anterior pero con el derecho
            arbol['der'] = nodoArbol()
        insertar_nodo(arbol['der'], dato, datos)
    balancear(arbol)
    actualizar_altura(arbol)


def altura(arbol):
    if arbol is None:
        return -1
    else:
        return arbol['altura']


def actualizar_altura(arbol):
    if arbol is not None:
        alt_izq = altura(arbol['izq'])  #si no hay diccionario creado retorna -1 si lo hay es cero
        alt_der = altura(arbol['der'])  #lo mismo
        arbol['altura'] = (alt_izq if alt_izq > alt_der else alt_der) + 1   #la altura mas grande se guarda creeo



def rotar_simple(arbol, control):
    aux = nodoArbol()
    if control:
        copiar_nodo(arbol['izq'], aux)
        arbol['izq'] = None
        if(aux['der'] and not arbol['izq']):
            arbol['izq'] = nodoArbol()
        copiar_nodo(aux['der'], arbol['izq'])
        aux['der'] = nodoArbol()
        copiar_nodo(arbol, aux['der'])
    else:
        copiar_nodo(arbol['der'], aux)
        arbol['der'] = None
        if(aux['izq'] and not arbol['der']):
            arbol['der'] = nodoArbol()
        copiar_nodo(aux['izq'], arbol['der'])
        aux['izq'] = nodoArbol()
        copiar_nodo(arbol, aux['izq'])
    arbol.update(aux)
    actualizar_altura(aux['izq'])
    actualizar_altura(aux['der'])
    actualizar_altura(aux)  ##porque actualiza la altura del aux?? no sera la del arbol?? si aux ya lo agrego a arbol por eso...buscar bien


def rotar_doble(arbol, control):
    if control:
        rotar_simple(arbol['izq'], False)
        rotar_simple(arbol, True)
    else:
        rotar_simple(arbol['der'], True)
        rotar_simple(arbol, False)


def balancear(arbol):
    if arbol is not None:
        if altura(arbol['izq']) - altura(arbol['der']) == 2:    #si una rama tiene 2 hijos mas de diferencia(creo)
            if(altura(arbol['izq']['izq']) >= altura(arbol['izq']['der'])):
                rotar_simple(arbol, True)
            else:
                rotar_doble(arbol, True)
        elif altura(arbol['der']) - altura(arbol['izq']) == 2:
            if(altura(arbol['der']['der']) >= altura(arbol['der']['izq'])):
                rotar_simple(arbol, False)
            else:
                rotar_doble(arbol, False)



def arbol_vacio(arbol):
    return arbol['info'] is None


def preorden(arbol):    #muestra la raiz y de ahi va mostrando hasta el mas chico luego va hacia los mayores
    if(arbol is not None):
        print(arbol['info'], arbol['altura'],
              arbol['izq']['info'] if arbol['izq'] else None,
              arbol['der']['info'] if arbol['der'] else None)
        preorden(arbol['izq'])
        preorden(arbol['der'])


def contar_heroes(arbol):
    contador = 0
    if(arbol is not None):
        if arbol['datos']['villano'] == False:
            contador += 1
        contador += contar_heroes(arbol['izq'])
        contador += contar_heroes(arbol['der'])
    return contador


def contar_heroes_villanos(arbol, resultados):
    if(arbol is not None):
        if arbol['datos']['villano'] == True:
            resultados['villanos'] += 1
        elif arbol['datos']['villano'] == False:
            resultados['heroes'] += 1
        contar_heroes_villanos(arbol['izq'], resultados)
        contar_heroes_villanos(arbol['der'], resultados)


def inorden(arbol):     #muestra los numeros de manera acendente(del mas chico al mas grande)
    if(arbol is not None):
        inorden(arbol['izq'])
        print(arbol['info'])
        inorden(arbol['der'])


def inorden_nrr(arbol):
    if(arbol is not None):
        inorden_nrr(arbol['izq'])
        print(arbol['info'], arbol['datos'])
        inorden_nrr(arbol['der'])


def inorden_villano(arbol):
    if(arbol is not None):
        inorden_villano(arbol['izq'])
        if arbol['villano'] == True:
            print(arbol['info'])
        inorden_villano(arbol['der'])


def inorden_empieza_con(arbol, valor):
    if(arbol is not None):
        inorden_empieza_con(arbol['izq'], valor)
        if arbol['info'].startswith(valor):
            print(arbol['info'])
        inorden_empieza_con(arbol['der'], valor)


def postorden(arbol):
    if(arbol is not None):
        postorden(arbol['der'])
        print(arbol['info'])
        postorden(arbol['izq'])


def postorden_heroes(arbol):
    if(arbol is not None):
        postorden_heroes(arbol['der'])
        if arbol['villano'] == False:
            print(arbol['info'])
        postorden_heroes(arbol['izq'])


def busqueda(arbol, clave):
    aux = None
    if arbol is not None and arbol['info'] is not None:
        if arbol['info'] == clave:
            aux = arbol
        elif clave < arbol['info']:
            aux = busqueda(arbol['izq'], clave)
        else:
            aux = busqueda(arbol['der'], clave)
    return aux


def remplazar(arbol, anterior=None, primero=None):  #es utilizado por esta clase nomas (tiene q ser privada)
    info, datos = None, None
    if arbol['der'] is None:
        info, datos = arbol['info'], arbol['datos']
        if anterior:
            anterior['der'] = arbol['izq']
        else:
            primero['izq'] = arbol['izq']
    else:
        info, datos = remplazar(arbol['der'], anterior=arbol)
    return info, datos


def eliminar_nodo(arbol, clave, previo=None, hijo=None):
    x, datos = None, None
    if arbol['info'] is not None:
        if arbol['izq'] and clave < arbol['info']:
            x, datos = eliminar_nodo(arbol['izq'], clave, arbol, 'izq')
        elif arbol['der'] and clave > arbol['info']:
            x, datos = eliminar_nodo(arbol['der'], clave, arbol, 'der')
        elif arbol['info'] == clave:
            x = arbol['info']
            datos = arbol['datos']
            if arbol['izq'] is None and arbol['der'] is not None:
                copiar_nodo(arbol['der'], arbol)
            elif arbol['der'] is None and arbol['izq'] is not None:
                copiar_nodo(arbol['izq'], arbol)
            elif arbol['izq'] is None and arbol['der'] is None:
                if previo is None:
                    arbol['info'] = None
                    arbol['datos'] = None
                else:
                    previo[hijo] = None
            else:
                info_aux, datos_aux = remplazar(arbol['izq'], primero=arbol)
                arbol['info'] = info_aux
                arbol['datos'] = datos_aux
        actualizar_altura(arbol)
        balancear(arbol)
    return x, datos


def por_nivel(arbol):
    pendientes = Cola()
    pendientes.arribo(arbol)
    while not pendientes.cola_vacia():
        nodo = pendientes.atencion()
        print(nodo['info'], nodo['izq']['info'] if nodo['izq'] else None, nodo['der']['info'] if nodo['der'] else None)
        if nodo['izq']:
            pendientes.arribo(nodo['izq'])
        if nodo['der']:
            pendientes.arribo(nodo['der'])


def crear_bosque(arbol, bosque1, bosque2):
    if(arbol is not None):
        crear_bosque(arbol['izq'], bosque1, bosque2)
        if arbol['datos']['villano'] == True:
            insertar_nodo(bosque2, arbol['info'])
        else:
            insertar_nodo(bosque1, arbol['info'])
        crear_bosque(arbol['der'], bosque1, bosque2)


############################################### MIS METODOS ####################################################
def altura_de_los_subarboles(arbol):
    if arbol['izq'] is not None:
        altura_izqui = arbol['izq']['altura']
    if arbol['der'] is not None:
        altura_derecha = arbol['der']['altura']
    return altura_izqui,altura_derecha

def cantidad_de_interaciones_de_un_elemento_x(arbol, clave):
    repetido=0
    if arbol is not None:
        repetido += cantidad_de_interaciones_de_un_elemento_x(arbol['izq'],clave) #va hacia el más chico hasta encontrar una hoja
        if arbol['info']==clave:    #luego compara su raiz 
            repetido +=1
        repetido += cantidad_de_interaciones_de_un_elemento_x(arbol['der'],clave)   #y pasa a comparar a sus derecha
    return repetido

def cantidad_de_elementos_guardados(arbol):
    cantidad=0
    if arbol is not None:
        cantidad += cantidad_de_elementos_guardados(arbol['izq']) 
        cantidad +=1
        cantidad += cantidad_de_elementos_guardados(arbol['der'])   
    return cantidad


def cantidad_de_numeros_pares(arbol):
    pares = 0
    if arbol is not None:
        pares += cantidad_de_numeros_pares(arbol['izq']) 
        if arbol['info'] % 2 == 0:     
            pares +=1
        pares += cantidad_de_numeros_pares(arbol['der'])   
    return pares

#funciona pero se puede mejorar aun mas (ya que sigue comparando una vez q lo encuentra y no tiene hijos izq y der)
def obtener_arbol_izq_y_der_de_un_nodo_x(arbol, clave):
    arbol_izquierdo,arbol_derecho= None,None
    if arbol is not None:
        arbol_izquierdo,arbol_derecho= obtener_arbol_izq_y_der_de_un_nodo_x(arbol['izq'],clave) #va hacia el más chico hasta encontrar una hoja
        if arbol['info']==clave:    #luego compara su raiz 
                arbol_izquierdo,arbol_derecho= nodoArbol(),nodoArbol()
                arbol_izquierdo = arbol['izq']
                arbol_derecho = arbol['der']
        elif arbol_izquierdo is None and arbol_izquierdo is None:   #para q va a seguir comparando si ya encontro el nodo
            arbol_izquierdo,arbol_derecho = obtener_arbol_izq_y_der_de_un_nodo_x(arbol['der'],clave)   #y pasa a comparar a sus derecha
    return arbol_izquierdo, arbol_derecho

#################-----METODOS PARA RESOLVER EL EJERCICIO 5  ----------##########################
def mostrar_alfabeticamente_los_villanos(arbol): #ascendente    
    if arbol is not None:
        mostrar_alfabeticamente_los_villanos(arbol['izq'])
        if arbol['datos'] == False:
            print(arbol['info'])
        mostrar_alfabeticamente_los_villanos(arbol['der'])

def mostrar_todos_los_perosonajes_que_empiezan_con_letra_x(arbol, clave):
    if arbol is not None:
        mostrar_todos_los_perosonajes_que_empiezan_con_letra_x(arbol['izq'], clave)
        if arbol['info'][0].upper() == clave.upper():
            print(arbol['info'])
        mostrar_todos_los_perosonajes_que_empiezan_con_letra_x(arbol['der'], clave)

def cantidad_de_elementos_personajes_guardados(arbol):
    cantidad=0
    if arbol is not None:
        cantidad += cantidad_de_elementos_personajes_guardados(arbol['izq']) 
        cantidad +=1
        cantidad += cantidad_de_elementos_personajes_guardados(arbol['der'])   
    return cantidad


def eliminar_personaje(arbol, clave, previo=None, hijo=None):
    x, datos = None, None
    if arbol['info'] is not None:
        if arbol['izq'] and clave.upper() < arbol['info'].upper():
            x, datos = eliminar_personaje(arbol['izq'], clave, arbol, 'izq')
        elif arbol['der'] and clave.upper() > arbol['info'].upper():
            x, datos = eliminar_personaje(arbol['der'], clave, arbol, 'der')
        elif arbol['info'].upper() == clave.upper():
            x = arbol['info']
            datos = arbol['datos']
            if arbol['izq'] is None and arbol['der'] is not None:
                copiar_nodo(arbol['der'], arbol)
            elif arbol['der'] is None and arbol['izq'] is not None:
                copiar_nodo(arbol['izq'], arbol)
            elif arbol['izq'] is None and arbol['der'] is None:
                if previo is None:
                    arbol['info'] = None
                    arbol['datos'] = None
                else:
                    previo[hijo] = None
            else:
                info_aux, datos_aux = remplazar(arbol['izq'], primero=arbol)
                arbol['info'] = info_aux
                arbol['datos'] = datos_aux
        actualizar_altura(arbol)
        balancear(arbol)
    return x, datos


def mostrar_todos_los_personajes_en_manera_descendente(arbol):    #descendente 
    if arbol is not None:
        mostrar_todos_los_personajes_en_manera_descendente(arbol['der'])
        print(arbol['info'])
        mostrar_todos_los_personajes_en_manera_descendente(arbol['izq'])

#generar un bosque
def generar_bosque_de_villanos_y_heroes(arbol, arbol_heroes,arbol_villanos):
    if arbol is not None:
        generar_bosque_de_villanos_y_heroes(arbol['izq'], arbol_heroes,arbol_villanos)
        if arbol['datos']== False:
            insertar_nodo(arbol_villanos, arbol['info'], arbol['datos'])
        else:
            insertar_nodo(arbol_heroes, arbol['info'], arbol['datos'])
        generar_bosque_de_villanos_y_heroes(arbol['der'], arbol_heroes,arbol_villanos)

def mostrar_alfabeticamente_todos_los_personajes(arbol): #ascendente    
    if arbol is not None:
        mostrar_alfabeticamente_todos_los_personajes(arbol['izq'])
        print(arbol['info'])
        mostrar_alfabeticamente_todos_los_personajes(arbol['der'])
#################-----ACÁ TERMINA LOS METODOS PARA RESOLVER EL EJERCICIO 5  ----------##########################

#################----- METODOS PARA RESOLVER EL EJERCICIO 6 (jedis)  ----------##########################
def inorden_alfabeticamente_todos_los_personajes_jedis(arbol): #ascendente    
    if arbol is not None:
        inorden_alfabeticamente_todos_los_personajes_jedis(arbol['izq'])
        print(arbol['info']," datos: ",arbol['datos'])
        inorden_alfabeticamente_todos_los_personajes_jedis(arbol['der'])

#ya cree uno mas "generico"(es el metodo siguiente) pero es poco "eficiente ya q crea una copia del dic de datos"
"""def generar_bosque_ordenaodo_por_ranking_y_especie(arbol, arbol_ranking,arbol_epecie):
    if arbol is not None:
        generar_bosque_ordenaodo_por_ranking_y_especie(arbol['izq'], arbol_ranking,arbol_epecie)

        datos_extras ={"especie":arbol['datos']['especie'] ,"año de nacimiento":arbol['datos']['año de nacimiento'],"color de sable de luz":arbol['datos']['color de sable de luz'],"nombre":arbol['info'],"maestros":arbol['datos']['maestros']}
        insertar_nodo(arbol_ranking, arbol['datos']['ranking'], datos_extras) #al ranking lo guardo en el lugar del info
        
        datos_extras ={"nombre":arbol['info'] ,"año de nacimiento":arbol['datos']['año de nacimiento'],"color de sable de luz":arbol['datos']['color de sable de luz'],"ranking":arbol['datos']['ranking'],"maestros":arbol['datos']['maestros']}
        insertar_nodo(arbol_epecie, arbol['datos']['especie'], datos_extras)  #al especie lo guardo en el lugar del info
        generar_bosque_ordenaodo_por_ranking_y_especie(arbol['der'], arbol_ranking,arbol_epecie)"""


#no es muy "eficiente" ya q creo una copia del dic datos (esto es porque si no la hago cuando intento eliminar una clave los dos se modifican por eso utlizo la .copy())
def generar_bosque_ordenaodo_por_x_dato(arbol, nuevo_arbol, dato_x):
    if arbol is not None:
        generar_bosque_ordenaodo_por_x_dato(arbol['izq'], nuevo_arbol,dato_x)
        #primero hay q verificar si el dato_x es realmente una clave guardada 
        #lo hago con el get ya q con el arbol[dato_x] me salta error si no encuentra la clave
        if arbol['datos'].get(dato_x) is not None:   #si existe la clave_x
            datos_para_nuevo_arbol=arbol['datos'].copy()    #una copia (porque sino se modifican los dos...)
            insertar_nodo(nuevo_arbol, arbol['datos'][dato_x], datos_para_nuevo_arbol) #al dato_x lo guardo en el lugar del info
            #eliminamos el elemento de la copia del dic de datos
            datos_para_nuevo_arbol.pop(dato_x)
            #agregamos el nombre a la copia del dic de datos(q es con lo q estaba ordenado originalmente)
            datos_para_nuevo_arbol['nombre']= arbol['info']
        generar_bosque_ordenaodo_por_x_dato(arbol['der'], nuevo_arbol,dato_x)

def mostrar_jedi_x(arbol,personaje): #ascendente
    encontrado = False   
    if arbol is not None:
        encontrado = mostrar_jedi_x(arbol['izq'], personaje)
        if arbol['info'].upper() == personaje.upper():
            print(arbol['info']," datos: ", arbol['datos'])
            encontrado = True
        elif (encontrado is False): #si ya lo encontro para q seguir buscando (se puede mejorar ya q sigue buscando todavia )
            encontrado = mostrar_jedi_x(arbol['der'], personaje)
    return encontrado

def mostrar_todos_los_jedis_con_x_ranking(arbol, clave):    
    if arbol is not None:
        mostrar_todos_los_jedis_con_x_ranking(arbol['izq'], clave)
        if clave.upper() in arbol['datos']['ranking'].upper():
            print(arbol['info']," datos: ",arbol['datos'])
        mostrar_todos_los_jedis_con_x_ranking(arbol['der'], clave)

def mostrar_todos_los_jedis_con_x_color_sable(arbol, clave):    
    if arbol is not None:
        mostrar_todos_los_jedis_con_x_color_sable(arbol['izq'], clave)
        if clave.upper() in arbol['datos']['color de sable de luz'].upper():
            print(arbol['info']," datos: ",arbol['datos'])
        mostrar_todos_los_jedis_con_x_color_sable(arbol['der'], clave)

def mostrar_todos_los_jedis_que_tengan_su_maestro_cargado(arbol):    
    if arbol is not None:
        mostrar_todos_los_jedis_que_tengan_su_maestro_cargado(arbol['izq'])
        if arbol['datos']['maestros'] is not '-':
            print(arbol['info']," datos: ",arbol['datos'])
        mostrar_todos_los_jedis_que_tengan_su_maestro_cargado(arbol['der'])

def mostrar_todos_los_jedis_de_especie_x_(arbol, clave):    
    if arbol is not None:
        mostrar_todos_los_jedis_de_especie_x_(arbol['izq'], clave)
        if clave.upper() in arbol['datos']['especie'].upper():
            print(arbol['info']," datos: ",arbol['datos'])
        mostrar_todos_los_jedis_de_especie_x_(arbol['der'], clave)

def mostrar_todos_los_jedis_que_empiecen_con_x_letra_o_q_tengan_un_guion_en_nombre(arbol, clave):    
    if arbol is not None:
        mostrar_todos_los_jedis_que_empiecen_con_x_letra_o_q_tengan_un_guion_en_nombre(arbol['izq'], clave)
        if clave.upper() in arbol['info'][0].upper() or '-' in arbol['info'].upper() :
            print(arbol['info']," datos: ",arbol['datos'])
        mostrar_todos_los_jedis_que_empiecen_con_x_letra_o_q_tengan_un_guion_en_nombre(arbol['der'], clave)
#################-----ACÁ TERMINA LOS METODOS PARA RESOLVER EL EJERCICIO 6  ----------##########################


#################----- METODOS PARA RESOLVER EL EJERCICIO 23  ----------##########################
def inorden_criaturas(arbol):     
    if(arbol is not None):
        inorden_criaturas(arbol['izq'])
        print(arbol['info'], 'datos: ',arbol['datos'])
        inorden_criaturas(arbol['der'])

def cargar_breve_descripcion_a_criatura_x(arbol, criatura,descripcion):     
    encontrado = False   
    if arbol is not None:
        encontrado = cargar_breve_descripcion_a_criatura_x(arbol['izq'], criatura, descripcion)
        if arbol['info'].upper() == criatura.upper():
            arbol['datos']['descripcion']=descripcion
            encontrado = True
        elif (encontrado is False): #si ya lo encontro para q seguir buscando (se puede mejorar ya q sigue buscando todavia )
            encontrado = cargar_breve_descripcion_a_criatura_x(arbol['der'], criatura, descripcion)
    return encontrado


def criaturas_con_breve_descripcion(arbol): 
    if arbol is not None:
        criaturas_con_breve_descripcion(arbol['izq'])
        if arbol['datos'].get("descripcion"):
            print(arbol['info']," datos: ", arbol['datos'])
        criaturas_con_breve_descripcion(arbol['der'])

def mostrar_criatura_x(arbol,criatura): #ascendente
    encontrado = False   
    if arbol is not None:
        encontrado = mostrar_criatura_x(arbol['izq'], criatura)
        if arbol['info'].upper() == criatura.upper():
            print(arbol['info']," datos: ", arbol['datos'])
            encontrado = True
        elif (encontrado is False): #si ya lo encontro para q seguir buscando (se puede mejorar ya q sigue buscando todavia )
            encontrado = mostrar_criatura_x(arbol['der'], criatura)
    return encontrado

####    objeto DIOS
class Dios:
    def __init__(self, nombre, canti_de_criaturas_derrotadas):
        self.nombre = nombre
        self.canti_de_criaturas_derrotadas = canti_de_criaturas_derrotadas
    
    def __str__(self):
        return f"{self.nombre},{self.canti_de_criaturas_derrotadas}"
####

def cambiar_cantidad_de_criaturas_derrotadas_de_la_lista(lista,nombre): #esto metodo solo lo utliza un metodo de esta clase
    i=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        if dato.nombre.upper()==nombre.upper(): #si el dios esta en la lista  lo debo eliminar e insertar de nuevo pero aumentadole la cantidad de veces q mato una criatura(para eso debo crear otro objeto dios)
            dios_nuevo= Dios(dato.nombre,dato.canti_de_criaturas_derrotadas+1)
            lista.eliminar(dato.nombre,'nombre')##elimino el dios
            lista.insertar(dios_nuevo,'canti_de_criaturas_derrotadas')#inserto el nuevo ya modificado
            
            return True #si retorna true es porque el dios ya estaba cargado
            #si lo encontro, ya no es necesario q siga comprbando(si se supone q no hay repetidos)
        else:                       #el break para el bucle
            i+=1    #aca si aumento i para q apunte al otro dato
    return False    #si retorna false es porque el dios no esta cargado en la lista

def mostrar_dios_con_mayor_criaturas_derrotadas_de_la_lista(lista):   #para mostrar el dios con mayor derrota
    i=0
    dato=lista.obtener_elemento(i)
    mayor=dato.canti_de_criaturas_derrotadas
    #lista.eliminar(dato.nombre,'nombre')
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        if dato.canti_de_criaturas_derrotadas > mayor:
            mayor=dato.canti_de_criaturas_derrotadas
        else:                       #el break para el bucle
            i+=1    #aca si aumento i para q apunte al otro dato    
    return dato


def pasar_dioses_a_lista_para_averiguar_mayor_captura_de_criaturas(arbol, lista_de_dioses):
    if arbol is not None:
        pasar_dioses_a_lista_para_averiguar_mayor_captura_de_criaturas(arbol['izq'],lista_de_dioses)
        if lista_de_dioses.lista_vacia():   #por ser el primer dios no le pongo q lo ordene (va a entrar una sola vez aca igual)
            lista_de_dioses.insertar(Dios(arbol['datos']['derrotado por'],1))
        elif cambiar_cantidad_de_criaturas_derrotadas_de_la_lista(lista_de_dioses, arbol['datos']['derrotado por']) is False and arbol['datos']['derrotado por'] != '-' :
            lista_de_dioses.insertar(Dios(arbol['datos']['derrotado por'],1),'canti_de_criaturas_derrotadas') #lo ordenamos por canti_de_criaturas_derrotadas   
        
        pasar_dioses_a_lista_para_averiguar_mayor_captura_de_criaturas(arbol['der'],lista_de_dioses)

def mostrar_todas_las_criaturas_derrotada_por_dios_x(arbol, clave): 
    if arbol is not None:
        mostrar_todas_las_criaturas_derrotada_por_dios_x(arbol['izq'], clave)
        if arbol['datos']['derrotado por'].upper() == clave.upper():
            print(arbol['info'])
        mostrar_todas_las_criaturas_derrotada_por_dios_x(arbol['der'], clave)

def mostrar_todas_las_criaturas_q_no_fueron_derrotadas(arbol): 
    if arbol is not None:
        mostrar_todas_las_criaturas_q_no_fueron_derrotadas(arbol['izq'])
        if arbol['datos']['derrotado por'] == '-':
            print(arbol['info'])
        mostrar_todas_las_criaturas_q_no_fueron_derrotadas(arbol['der'])


def agregar_campo_capturadas_a_todas_las_criaturas(arbol): 
    if arbol is not None:
        agregar_campo_capturadas_a_todas_las_criaturas(arbol['izq'])
        arbol['datos']['capturada']= None
        agregar_campo_capturadas_a_todas_las_criaturas(arbol['der'])

def modificar_el_campo_capturada_de_x_criatura(arbol, criatura, clave): 
    encontrado = False
    if arbol is not None:
        encontrado = modificar_el_campo_capturada_de_x_criatura(arbol['izq'], criatura, clave)
        if arbol['info'].upper() == criatura.upper():
            arbol['datos']['capturada'] = clave
            encontrado = True
        elif (encontrado is False): #si ya lo encontro para q seguir buscando (se puede mejorar ya q sigue buscando todavia )
            encontrado = modificar_el_campo_capturada_de_x_criatura(arbol['der'], criatura, clave)
    return encontrado

def busqueda_por_coincidencia(arbol, clave): 
    if arbol is not None:
        busqueda_por_coincidencia(arbol['izq'], clave)
        #if en una sola linea
        print(arbol['info'],'datos: ',arbol['datos']) if clave.upper() in arbol['datos']['derrotado por'].upper() else None
        if clave.upper() in arbol['info'].upper() or clave.upper() in arbol['datos']['capturada'].upper() if arbol['datos']['capturada'] is not None else None:
            print(arbol['info'],'datos: ',arbol['datos'])
        if arbol['datos'].get('descripcion'): #porque no a todos le agregue el campo descripcion
            if clave.upper() in arbol['datos']['descripcion'].upper():
                print(arbol['info'],'datos: ',arbol['datos'])
        busqueda_por_coincidencia(arbol['der'], clave)


def modificar_el_campo_derrotado_de_x_criatura(arbol, criatura, clave): 
    encontrado = False
    if arbol is not None:
        encontrado = modificar_el_campo_derrotado_de_x_criatura(arbol['izq'], criatura, clave)
        if arbol['info'].upper() == criatura.upper():
            arbol['datos']['derrotado por'] = clave
            encontrado = True
        elif (encontrado is False): #si ya lo encontro para q seguir buscando (se puede mejorar ya q sigue buscando todavia )
            encontrado = modificar_el_campo_derrotado_de_x_criatura(arbol['der'], criatura, clave)
    return encontrado

def modificar_el_campo_info_de_x_criatura(arbol, criatura, nuevo_nombre): #como el arbol esta ordenado por el campo info tendremos q eliminar el nodo y cargarlo de nuevo con la nueva info
    info, datos =eliminar_nodo(arbol,criatura)
    if info is not None:
        insertar_nodo(arbol, nuevo_nombre, datos)

def mostrar_todas_las_criaturas_q_fueron_capturada_por_x_dios(arbol, dios): 
    if arbol is not None:
        mostrar_todas_las_criaturas_q_fueron_capturada_por_x_dios(arbol['izq'], dios)
        if arbol['datos']['capturada'] is not None:
            if arbol['datos']['capturada'].upper() == dios.upper():
                print(arbol['info'],'datos: ',arbol['datos'])
        mostrar_todas_las_criaturas_q_fueron_capturada_por_x_dios(arbol['der'], dios)

#################-----ACÁ TERMINA LOS METODOS PARA RESOLVER EL EJERCICIO 23  ----------##########################
# arb = nodoArbol()

# insertar_nodo(arb, 1)
# insertar_nodo(arb, 3)
# insertar_nodo(arb, 2)
# insertar_nodo(arb, 4)
# insertar_nodo(arb, 5)
# insertar_nodo(arb, 6)
# insertar_nodo(arb, 7)
# insertar_nodo(arb, 8)
# insertar_nodo(arb, 9)
# insertar_nodo(arb, 10)
# insertar_nodo(arb, 11)
# insertar_nodo(arb, 12)
# insertar_nodo(arb, 13)
# insertar_nodo(arb, 14)
# insertar_nodo(arb, 15)

# print()
# preorden(arb)
# print(arbol)
# insertar_nodo(arbol, 19)
# insertar_nodo(arbol, 7)
# insertar_nodo(arbol, 1)
# insertar_nodo(arbol, 31)
# insertar_nodo(arbol, 22)
# insertar_nodo(arbol, 45)
# insertar_nodo(arbol, 27)    
# insertar_nodo(arbol, 24) 


# preorden(arbol)

# value = eliminar_nodo(arbol, 31)

# print('valor eliminado', value)

# preorden(arbol)

# por_nivel(arbol)

# pos = busqueda(arbol, 45)
# if pos:
#     print('asdasd', pos['info'])

# postorden(arbol)