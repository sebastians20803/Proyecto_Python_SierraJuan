from datetime import datetime, timedelta
from tabulate import tabulate
import loadsavefiles

def listar_gasto (gastos_lista):

    loadsavefiles.limpiar_pantalla()
    print (" ============================================")
    print ("            LISTAR GASTOS            ")
    print (" ============================================")
    print ("Seleccione una opcion para filtrar los gastos: ")
    print ("")
    print ("1. Ver todos los gastos:  ")
    print ("2. Filtrar por categoria:  ")
    print ("3. Filtrar por rango de fechas")
    print ("4. Ver desglose por categoria")
    print ("5. Regresar al menu principal")

    print (" =================================================")

    try:
        opcion =int(input("Digite la opcion que desea realizar: "))
        if opcion == 1:
            if gastos_lista:
                print(tabulate(gastos_lista, headers="keys", tablefmt="grid"))
            else:
                print("No hay gastos registrados")
            loadsavefiles.pausa()
        elif opcion == 2:
            loadsavefiles.limpiar_pantalla()
            print (" ============================================")
            print ("     SELECCIONE LA CATEGORIA A FILTRAR       ")
            print (" ============================================")
            print ("Seleccione una opcion para filtrar los gastos: ")
            print ("")
            print ("1. Comida  ")
            print ("2. Transporte ")
            print ("3. Entretenimiento ")
            print ("4. Otros")

            print (" =================================================")
            try: #
                opcion_categoria = int (input("Digite la opcion que desea realizar: "))
                lista_filtrada_categoria = []
                for i in gastos_lista:
                    if opcion_categoria == 1 and i["categoria"] == "Comida":
                        lista_filtrada_categoria.append(i)
                    elif opcion_categoria == 2 and i["categoria"] == "Transporte":
                        lista_filtrada_categoria.append(i)    
                    elif opcion_categoria == 3 and i["categoria"] == "Entretenimiento":
                        lista_filtrada_categoria.append(i)                      
                    elif opcion_categoria == 4 and i["categoria"] == "Otros":
                        lista_filtrada_categoria.append(i)
                if opcion_categoria < 1 or opcion_categoria > 4:
                    print("Opcion no esta en el rango.")
                    loadsavefiles.pausa()
                    return
                if lista_filtrada_categoria:
                    print(tabulate(lista_filtrada_categoria,headers="keys", tablefmt="grid"))
                else:
                    print ("No hay gastos en la categoria seleccionada")    
                loadsavefiles.pausa()
                
                        
            except ValueError:
                print ("Debe digitar una cantidad numerica")
                loadsavefiles.pausa()
                return
            except Exception as e:
                print (f" Error {e}")
                loadsavefiles.pausa()
                return
        elif opcion == 3:
            try:
                print ("")
                fecha_inicio = input ("Ingrese la fecha de inicio de los gastos que desea ver en formato: AAAA-MM-DD:  ") 
                fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d") 
                print ("Fecha correcta")    
            except ValueError:
                print("Formato incorrecto. Debe ser AAAA-MM-DD")  
                loadsavefiles.pausa()
                return  
            print ("\n Ingrese 'S' para continuar con la fecha final o 'C' para cancelar. ")
            print ("")
            opc_fecha=input("").capitalize().strip()
            if opc_fecha == "S":
                try:
                    print ("")
                    fecha_final = input ("Ingrese la fecha final de los gastos que desea ver en formato: AAAA-MM-DD: ")  
                    print ("")
                    fecha_final_dt = datetime.strptime(fecha_final, "%Y-%m-%d")
                except ValueError:
                    print("Formato incorrecto. Debe ser AAAA-MM-DD")
                    loadsavefiles.pausa()
                    return 
                
                lista_filtrada_fecha = []
                for i in gastos_lista:
                    fecha_i = datetime.strptime(i["fecha"], "%Y-%m-%d")
                    if fecha_inicio_dt <= fecha_i <= fecha_final_dt:
                        lista_filtrada_fecha.append(i)
                if lista_filtrada_fecha:
                    print ("")
                    print (f" La fecha de inicio es {fecha_inicio} y la fecha final {fecha_final}")  
                    print ("")
                    print (tabulate(lista_filtrada_fecha,headers="keys", tablefmt="grid"))
                else:
                    print ("No hay gastos en el rango seleccionado")
                loadsavefiles.pausa()
                
                         
            elif opc_fecha == "C":
                print ("VOLVIENDO AL MENU PRINCIPAL")
                loadsavefiles.pausa()
                return
            else:
                print("Opcion no valida")
                loadsavefiles.pausa()
                return
        elif opcion == 4:
        
            
            totales_por_categoria = {
                "Comida": 0,
                "Transporte": 0,
                "Entretenimiento": 0,
                "Otros": 0
            }
            
            for i in gastos_lista:
                totales_por_categoria [   i["categoria"]    ] += i["monto"] 
                #Voy a reemplazar la clave del diccionario totales_por_categoria dependiendo i donde estè:
                #Ejemplo: si cuando i en el primer diccionar i la categoria de ese gasto es de "Comida" pues se va sumar el monto que aparece en el diccionario
                
            print("\nGastos por categoría:")
            for i,k in totales_por_categoria.items():
                print(f"{i}: {k}") 
            
            loadsavefiles.pausa()
            
            
        elif opcion == 5:
            print("\n Volviendo al menu principal")
            loadsavefiles.pausa()
            return
        else:
            print ("\n Opcion no valida, volviendo al menu principal")
            loadsavefiles.pausa()
            return
    except Exception as e:
        print(f"Error: {e}")
        loadsavefiles.pausa()
        return
