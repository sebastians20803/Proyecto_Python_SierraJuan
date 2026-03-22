import os
import json

ARCHIVO = "gastostotales.json"

def cargar_archivo():
    try:
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO,"r") as f:
                return json.load(f)
        else:
            return []
    except json.JSONDecodeError:
        print ("Error: El archivo JSON esta dañado")
        return [] 
    except Exception as e:
        print(f"Error al cargar archivo: {e}")
        return []
#GUARDAR ARCHIVO JSON

def guardar_archivo(gastos_lista):
    with open (ARCHIVO, "w") as f:
        json.dump(gastos_lista,f, indent=4)
        
        
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def pausa():
    input("\nPresione ENTER para continuar...")