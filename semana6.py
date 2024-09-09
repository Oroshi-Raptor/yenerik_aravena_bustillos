import json
import os

# Definición de rutas de archivos
medicamentos_file = 'medicamentos.json'
laboratorios_file = 'laboratorios.json'

# Función para cargar datos de un archivo JSON
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return []

# Función para guardar datos en un archivo JSON
def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Inicializar datos de medicamentos y laboratorios
medicamentos = load_data(medicamentos_file)
laboratorios = load_data(laboratorios_file)

# Función para agregar un medicamento
def agregar_medicamento():
    nombre = input("Nombre del medicamento: ")
    tipo = input("Tipo de medicamento: ")
    cantidad = int(input("Cantidad de medicamento: "))
    
    medicamento = {
        "nombre": nombre,
        "tipo": tipo,
        "cantidad": cantidad
    }
    medicamentos.append(medicamento)
    save_data(medicamentos_file, medicamentos)
    print("Medicamento agregado exitosamente.")

# Función para agregar un laboratorio
def agregar_laboratorio():
    nombre = input("Nombre del laboratorio: ")
    ubicacion = input("Ubicación del laboratorio: ")
    
    laboratorio = {
        "nombre": nombre,
        "ubicacion": ubicacion
    }
    laboratorios.append(laboratorio)
    save_data(laboratorios_file, laboratorios)
    print("Laboratorio agregado exitosamente.")

# Función para mostrar los medicamentos
def mostrar_medicamentos():
    if medicamentos:
        print("Medicamentos almacenados:")
        print(json.dumps(medicamentos, indent=4))
    else:
        print("No hay medicamentos almacenados.")

# Función para mostrar los laboratorios
def mostrar_laboratorios():
    if laboratorios:
        print("Laboratorios almacenados:")
        print(json.dumps(laboratorios, indent=4))
    else:
        print("No hay laboratorios almacenados.")

# Función principal para interactuar con el usuario
def main():
    while True:
        print("\nMenú:")
        print("1. Agregar Medicamento")
        print("2. Agregar Laboratorio")
        print("3. Mostrar Medicamentos")
        print("4. Mostrar Laboratorios")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_medicamento()
        elif opcion == "2":
            agregar_laboratorio()
        elif opcion == "3":
            mostrar_medicamentos()
        elif opcion == "4":
            mostrar_laboratorios()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
