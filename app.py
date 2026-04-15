import json
import os

# Archivo donde se guardan las tareas
FILE = "tasks.json"


def load_tasks():
    """
    Carga las tareas desde el archivo JSON.
    Si el archivo no existe, devuelve una lista vacía.
    """
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    """
    Guarda la lista de tareas en el archivo JSON.
    """
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    """
    Agrega una nueva tarea a la lista.
    """
    title = input("Ingrese la tarea: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Tarea agregada correctamente.\n")


def list_tasks(tasks):
    """
    Muestra todas las tareas con su estado.
    """
    if not tasks:
        print("No hay tareas.\n")
        return

    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✘"
        print(f"{i + 1}. [{status}] {task['title']}")
    print()


def complete_task(tasks):
    """
    Marca una tarea como completada.
    """
    list_tasks(tasks)
    index = int(input("Número de tarea a completar: ")) - 1

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Tarea completada.\n")
    else:
        print("Índice inválido.\n")


def delete_task(tasks):
    """
    Elimina una tarea de la lista.
    """
    list_tasks(tasks)
    index = int(input("Número de tarea a eliminar: ")) - 1

    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Tarea eliminada.\n")
    else:
        print("Índice inválido.\n")


def main():
    """
    Función principal que maneja el menú.
    """
    tasks = load_tasks()

    while True:
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            add_task(tasks)
        elif option == "2":
            list_tasks(tasks)
        elif option == "3":
            complete_task(tasks)
        elif option == "4":
            delete_task(tasks)
        elif option == "5":
            break
        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    main()