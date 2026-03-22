from datetime import datetime, timedelta
from tabulate import tabulate
import loadsavefiles

def calcular_gasto(gastos_lista):
    
    loadsavefiles.limpiar_pantalla()
    print (" ============================================")
    print ("         CALCULAR TOTAL DE GASTOS            ")
    print (" ============================================")
    print ("Seleccione el periodo de calculo: ")
    print ("")
    print ("1. Calcular total diario:  ")
    print ("2. Calcular total semanal:  ")
    print ("3. Calcular total mensual:  ")
    print ("4. Regresar al menu principal")

    print (" =================================================")
    
    try:
        opcion =int(input("Digite la opcion que desea realizar: "))
        
    except ValueError: 
        print(f"Error: Debe digitar una cantidad numerica")
        loadsavefiles.pausa()
        return    
    lista_gastos_periodo = []
    totales_por_categoria = {
            "Comida": 0,
            "Transporte": 0,
            "Entretenimiento": 0,
            "Otros": 0
        }
    if opcion == 1:
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        for i in gastos_lista:
            if i["fecha"] == fecha_actual:
                lista_gastos_periodo.append(i["monto"])
                totales_por_categoria[i["categoria"]] += i["monto"]
        print ("")          
        print (f"Los gastos diarios de {fecha_actual} es de {sum(lista_gastos_periodo)}")
        print("\nGastos por categoría:")
        for i,k in totales_por_categoria.items():
            print(f"{i}: {k}")
        loadsavefiles.pausa()
    elif opcion == 2:
        fecha_actual = datetime.now() 
        nueva_fecha = fecha_actual - timedelta(days=7)
        for i in gastos_lista:
            fecha_i = datetime.strptime(i["fecha"], "%Y-%m-%d")
            if nueva_fecha<=fecha_i<=fecha_actual:
                lista_gastos_periodo.append (i["monto"])
                totales_por_categoria[i["categoria"]] += i["monto"]
        print ("")
        print (f"Los gastos de los ultimos 7 dias son de  {sum(lista_gastos_periodo)}")   
        print("\nGastos por categoría:")
        for i,k in totales_por_categoria.items():
            print(f"{i}: {k}") 
        loadsavefiles.pausa()    
    elif opcion == 3:
        
        fecha_actual = datetime.now()
        inicio_mes = fecha_actual.replace(day=1)

        for i in gastos_lista:
            fecha_i = datetime.strptime(i["fecha"], "%Y-%m-%d")
            if inicio_mes <= fecha_i <= fecha_actual:
                lista_gastos_periodo.append(i["monto"])
                totales_por_categoria[i["categoria"]] += i["monto"]
        print ("")
        print(f"Los gastos del mes actual son {sum(lista_gastos_periodo)}")
        print("\nGastos por categoría:")
        for i,k in totales_por_categoria.items():
            print(f"{i}: {k}")
        loadsavefiles.pausa()    
    elif opcion == 4:
        print("Volviendo al menu")
        loadsavefiles.pausa()
        return
    else:
        print("Opcion no valida")
        loadsavefiles.pausa()
        return

