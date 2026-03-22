from datetime import datetime, timedelta
import loadsavefiles

def registrar_gasto (gastos_lista):
    
    fecha_actual = datetime.now().strftime("%Y-%m-%d")

    loadsavefiles.limpiar_pantalla()
    print (" ============================================")
    print ("            REGISTRAR NUEVO GASTO            ")
    print (" ============================================")
    print ("Ingrese la informacion del gasto: ")
    print ("")
    print ("1. Monto del gasto:  ")
    print ("2. Categoria (ej. comida, transporte, entretenimiento, otros):  ")
    print ("3. Descripcion (opcional): ")

    print ("\n Ingrese 'S' para continuar o 'C' para cancelar. ")
    print (" =================================================")

    opcion_gasto = input("Digite lo que desea hacer: ").strip().upper()
    if opcion_gasto == "C":
        print ("\n Volviendo al menu anterior")
        loadsavefiles.pausa()
        return
    elif opcion_gasto == "S":
        try:
            monto=int(input("Digite el monto del gasto a agregar: $ "))
            if monto<=0:
                print("El monto debe ser mayor a cero")
                loadsavefiles.pausa()
                return
    
        except ValueError:
            print ("Debe digitar una cantidad numerica")
            loadsavefiles.pausa()
            return
        except Exception as i:
            print (f" Error {i}")
            loadsavefiles.pausa()
            return
            
            
        try:
            loadsavefiles.limpiar_pantalla()
            print (" ============================================")
            print ("             CATEGORIA DEL GASTO             ")
            print (" ============================================")
            print ("")
            print ("1. Comida")
            print ("2. Transporte")
            print ("3. Entretenimiento")
            print ("4. Otros ")

            opcion_categoria= int(input("\n Digite el numero de la categoria del gasto: "))
            if opcion_categoria == 1:
                categoria = "Comida"
            elif opcion_categoria==2:
                categoria = "Transporte"
            elif opcion_categoria==3:
                categoria= "Entretenimiento"
            elif opcion_categoria==4:
                categoria = "Otros"
            else:
                print("Debe digitar una numero entre 1 al 4")
                loadsavefiles.pausa()
                return
        except ValueError:
            print ("Debe digitar una numero entre 1 al 4")
            loadsavefiles.pausa()
            return
        except Exception as i:
            print (f" Error {i}")
            loadsavefiles.pausa()
            return
        try:
            loadsavefiles.limpiar_pantalla()
            print (" ============================================")
            print ("            DESCRIPCION DEL GASTO            ")
            print (" ============================================")
            print ("")
            print (" Desea ingresar una descripcion? ")
            print (" \n Escriba 'S' para agregar descripcion o 'C' sin descripcion  ")
            opcion_descripcion= input("Escriba S o C: ").capitalize().strip()
            descripcion_producto = ""
            if opcion_descripcion == "C":
                descripcion_producto = "N/A"

            elif opcion_descripcion == "S":
                descripcion_producto = input("\nDigite la descripcion del producto: ")
            else:
                print( "OPCION NO VALIDA")
                loadsavefiles.pausa()
                return
        except Exception as e:
            print(f"Error: {e}")
            loadsavefiles.pausa()
    else: 
        print("OPCION INVALIDA")
        loadsavefiles.pausa()
        return
    gasto = {
        "fecha" : fecha_actual,
        "monto" : monto,
        "categoria" : categoria,
        "descripcion" : descripcion_producto

    }

    gastos_lista.append(gasto)
    loadsavefiles.guardar_archivo(gastos_lista)
    print ("GASTO REGISTRADO CON EXITO!!! ")
    loadsavefiles.pausa()
   

    
