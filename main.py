import loadsavefiles,registrargasto,listargasto,calculargasto,generarreporte

def menu():
    
    while True:
        gastos_lista = loadsavefiles.cargar_archivo()
        loadsavefiles.limpiar_pantalla()

        print (" ============================================")
        print ("          SIMULADOR DE GASTO DIARIO          ")
        print (" ============================================")
        print ("Seleccione una opcion: ")
        print ("")
        print ("1. Registrar nuevo gasto  ")
        print ("2. Listar gastos  ")
        print ("3. Calcular total de gastos  ")
        print ("4. Generar reporte de gastos ")
        print ("5. Salir ")

        print (" ============================================")
        
        try:
            opcion = int(input("Digite la opcion: "))
        except (TypeError, ValueError):
            print("Opcion no valida")
            loadsavefiles.pausa()
            continue
        except Exception as e:
            print(f"ERROR: {e}")
            loadsavefiles.pausa()
            continue
        
        if opcion == 1:
            registrargasto.registrar_gasto(gastos_lista)
        elif opcion ==2:
            listargasto.listar_gasto(gastos_lista)
        elif opcion ==3:
            calculargasto.calcular_gasto(gastos_lista)
        elif opcion ==4:
            generarreporte.generar_reporte(gastos_lista)
        elif opcion ==5:
            try:
                opc_salir=input(" ¿Desea salir del programa? (S/N): "). capitalize()
                if opc_salir == "S":
                    print ("SALIENDO, GRACIAS POR USAR NUESTRO PROGRAMA ")
                    break
                elif opc_salir == "N":
                    print ("VOLVIENDO AL MENU PRINCIPAL")
                    loadsavefiles.pausa()
                    continue
                else:
                    print("Opcion no valida")
                    loadsavefiles.pausa()
            except ValueError:
                print ("Error: Opcion no valida")
                loadsavefiles.pausa()
                
        else:
            print("Opcion invalida")
            loadsavefiles.pausa()
            
if __name__ == "__main__":
    menu()