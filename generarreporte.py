import json

from datetime import datetime, timedelta
from tabulate import tabulate
import loadsavefiles

def generar_reporte(gastos_lista):
    loadsavefiles.limpiar_pantalla()
    print("=============================================")
    print("         Generar Reporte de Gastos           ")
    print("=============================================")
    print("Seleccione el tipo de reporte:")
    print("")
    print("1. Reporte diario")
    print("2. Reporte semanal")
    print("3. Reporte mensual")
    print("4. Regresar al menu principal")
    print("=============================================")
    try:
        opcion =int(input("Digite la opcion que desea realizar: "))
        filtro_gastos_periodo = []
        fecha_actual= datetime.now()
        
    except (TypeError, ValueError):
            print("Opcion no valida")
            loadsavefiles.pausa()
            return
    except Exception as e:
            print(f"ERROR: {e}")
            loadsavefiles.pausa()
            return
        
    if opcion == 1:
        nombre_reporte = "REPORTE DE HOY"
        fecha_a_str = fecha_actual.strftime("%Y-%m-%d")
        for i in gastos_lista:
            if i["fecha"] == fecha_a_str:
                filtro_gastos_periodo.append(i)
    elif opcion == 2:
        
        nombre_reporte = "REPORTE SEMANAL"
        fecha_inicio = fecha_actual - timedelta(days=7)

        for i in gastos_lista:
            fecha_i = datetime.strptime(i["fecha"], "%Y-%m-%d")
            if fecha_inicio <= fecha_i <= fecha_actual:
                filtro_gastos_periodo.append(i)

    elif opcion == 3:
        nombre_reporte = "REPORTE DEL MES ACTUAL"
        inicio_mes = fecha_actual.replace(day=1)

        for i in gastos_lista:
            fecha_i = datetime.strptime(i["fecha"], "%Y-%m-%d")
            if inicio_mes <= fecha_i <= fecha_actual:
                filtro_gastos_periodo.append(i)    
        
    elif opcion == 4:
        print ("Regresando al menu principal")
        loadsavefiles.pausa()
        return

    else:
        print("Opcion invalida")
        loadsavefiles.pausa()
        return
    # SUMAR GASTOS TOTALES EN LA NUEVA LISTA DEPENDIENDO EL RANGO
    suma_gastos_total = 0
    for i in filtro_gastos_periodo:
        suma_gastos_total+= i["monto"]  
    # SUMAR GASTOS POR CATEGORIA EN LA NUEVA LISTA DEPENDIENDO EL RANGO    
    total_gastado_categoria = {
                    "Comida": 0,
                    "Transporte": 0,
                    "Entretenimiento": 0,
                    "Otros": 0
                }
    for i in filtro_gastos_periodo:
        total_gastado_categoria[ i["categoria"] ] += i["monto"]
        
    
    reporte = {
        "tipo_reporte": nombre_reporte,
        "fecha_generacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cantidad_gastos": len(filtro_gastos_periodo),
        "total_gastado": suma_gastos_total,
        "total_gastado_categoria":total_gastado_categoria,
        "gastos":  filtro_gastos_periodo

    }
    loadsavefiles.limpiar_pantalla()    
    print("=============================================")
    print("              OPCIONES DE REPORTE            ")
    print("=============================================")
    print("1. Ver reporte en pantalla")
    print("2. Guardar reporte en archivo JSON")
    try:
        opc_reporte = int(input("Seleccione una opcion: "))
    except (TypeError, ValueError):
        print("Opcion no valida")
        loadsavefiles.pausa()
        return   
        
    if opc_reporte==1:
        
        loadsavefiles.limpiar_pantalla()
        print("=============================================")
        print(f"Tipo de reporte: {reporte ['tipo_reporte']}")
        print("=============================================")
        print(f"Fecha de generacion: {reporte['fecha_generacion']}")
        print(f"Cantidad de gastos: {reporte['cantidad_gastos']}")
        print(f"Total gastado: {reporte['total_gastado']}")
        print(f"\n Total gastado por categoria\n")
        for clave,valor in total_gastado_categoria.items():
            print (f"{clave} : {valor}")
            
        print("\n")
        if filtro_gastos_periodo:
            print(tabulate(filtro_gastos_periodo, headers="keys", tablefmt="grid"))
            
        else: print ("No hay gastos registrados en este periodo")
        loadsavefiles.pausa()
        
    elif opc_reporte==2:
        prenombre = reporte["tipo_reporte"].lower().replace(" ","_")
        nombre_archivo= f"{prenombre}.json"
        with open(nombre_archivo,"w") as archivo:
            json.dump (reporte,archivo,indent=4, ensure_ascii=False)
        print(f"Reporte guardado como {nombre_archivo}")
        loadsavefiles.pausa()
    else: 
        print("Opcion invalida")
        loadsavefiles.pausa()
        return
    