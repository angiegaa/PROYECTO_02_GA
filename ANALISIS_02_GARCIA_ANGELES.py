#register_id,direction,origin,destination,year,date,product,transport_mode,company_name,total_value

import csv

archivo_csv = open("synergy_logistics_database.csv")

database = []

with open("synergy_logistics_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)

    for linea in lector:
        database.append(linea)
        #print(linea)
        
#OPCIÓN 1        
#Se genera una nueva lista para poder utilizar la base de datos y ordenarse

#Se generan las rutas de exportación 
direction = "Exports"
contador = 0 
rutas_cont = []
rutas_total = []
suma = 0 
valor = 0
#Se definen dos listas para añadir las rutas 
for ruta in database:
    if ruta[1] == direction:
        rutas = [ruta[2], ruta[3]]
        
        if rutas not in rutas_cont:
            for destino in database:
                if rutas == [destino[2], destino[3]]:
                    contador += 1
                    suma += int(ruta[9])
                    
                    
    
            rutas_cont.append(rutas)
            formato = [ruta[2], ruta[3], contador, suma]
            rutas_total.append(formato)
            contador = 0
            
          
rutas_total.sort(reverse = True, key = lambda x:x[3])
#Los valores salen ordenados por el valor total de las exportaciones 

#Se generan las rutas de importación

direction_imp = "Imports"
contador = 0 
rutas_cont_1 = []
rutas_total_1 = []
suma_1 = 0 
valor_1 = 0
#Se definen dos listas para añadir las rutas 
for ruta in database:
    if ruta[1] == direction_imp:
        rutas = [ruta[2], ruta[3]]
        
        if rutas not in rutas_cont:
            for destino in database:
                if rutas == [destino[2], destino[3]]:
                    contador += 1
                    suma_1 += int(ruta[9])
                    
                    
    
            rutas_cont_1.append(rutas)
            formato2 = [ruta[2], ruta[3], contador, suma]
            rutas_total_1.append(formato2)
            contador = 0
            
          
rutas_total_1.sort(reverse = True, key = lambda x:x[3])
#Los valores salen ordenados por el valor total de las importaciones

#OPCIÓN 2 - MEDIOS DE TRANSPORTE

#Se genera una lista donde se conozcan primero cuales son los medios de transporte

transport_m = []

for transporte in database:
    mode = transporte[7]
    if mode not in transport_m:
        transport_m.append(mode)

#Se hace una lista de exportaciones completa considerando los datos completos

lista_exportaciones = []
for exports in database:
    if exports[1] == "Exports":
        lista_exportaciones.append(exports)
    
      
#Ahora se hace una lista con las exportaciones por medio de transporte

export_mode = []

for mode in transport_m:
    contador = 0
    valor = 0 

    for exportaciones in lista_exportaciones:
        transportm = exportaciones[7]
        if mode == transportm:
            contador += 1
            valor += int(exportaciones[9])
    formato_2 = [mode, contador, valor]           
    export_mode.append(formato_2)

export_mode.sort(reverse = True, key = lambda x:x[2])

#Se hace una lista de importaciones completa considerando los datos completos

lista_import = []
for imports in database:
    if imports[1] == "Imports":
        lista_import.append(imports)          
    
#Ahora se hace una lista con las exportaciones por medio de transporte

import_mode = []

for mode in transport_m:
    contador = 0
    valor = 0 

    for importaciones in lista_import:
        transportim = importaciones[7]
        if mode == transportim:
            contador += 1
            valor += int(importaciones[9])
    formato_2 = [mode, contador, valor]           
    import_mode.append(formato_2)

import_mode.sort(reverse = True, key = lambda x:x[2])

#OPCIÓN 3 - VALOR TOTAL DE LAS IMPORTACIONES Y EXPORTACIONES
#Se hizo primero una lista con el valor total de las importaciones y exportaciones 
            

imports = [] 

for linea in lista_import:
    imports.append(int(linea[9]))
            
            
print("El total de las importaciones es: ", sum(imports))

exports = []

for linea in lista_exportaciones:
    exports.append(int(linea[9]))

print("El total de las exportaciones es: ", sum(exports))


#Ahora se buscarán las exportaciones e importaciones por país determinado por su valor

#EXPORTACIONES POR PAÍS
#Se genera primero una lista con todos los países que tienen origen
#Exportaciones son los bienes y servicios de un país que se envían a otro
origen_p = []

for indice in lista_exportaciones:
    origen = indice[2]
    if origen not in origen_p:
        origen_p.append(origen)
        
#Se genera una lista a partir de origen_p para que se dé un valor total
#de las exportaciones por cada país

countryexp_value = []

for pais in origen_p:
    sumav = 0
    for exports in lista_exportaciones:
        if exports[2] == pais:
            sumav += int(exports[9])
    countryexp_value.append([pais, sumav])

countryexp_value.sort(reverse = True, key = lambda x:x[1])

#IMPORTACIONES POR PAÍS
#Se genera primero una lista con todos los países que tienen destino
#Importaciones son los bienes y servicios de un país que se ingresan de otro p
destino_p = []

for indice in lista_import:
    destino = indice[2]
    if destino not in destino_p:
        destino_p.append(destino)

#Se genera una lista a partir de origen_p para que se dé un valor total
#de las importaciones por cada país

countryimp_value = []

for pais in destino_p:
    sumac = 0
    for imports in lista_import:
        if imports[2] == pais:
            sumac += int(imports[9])
    countryimp_value.append([pais, sumac])
    
countryimp_value.sort(reverse = True, key = lambda x:x[1])















        
        

