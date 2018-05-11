import argparse
import os

parser = argparse.ArgumentParser(description="crea una nueva clase del modulo")

parser.add_argument("title", type=str,
                    help="Titulo de la clase entre comillas")
parser.add_argument("-n", "--number", type=int,
                    help="Numero de sesión a crear")
args = parser.parse_args()

title = args.title
number = args.number

session_template = """
# {}

**Módulo III - Proyectos reales**

## Objetivos

## Descripción corta

## Actividades

* **nombre actividad**: descripción

## Conceptos

## Material

## Tareas
""".format(title)

if number:
    if abs(number) < 10:
        session_number = "0{}".format(abs(number))
    else:
        session_number = "{}".format(abs(number))

else:
    session_number = ""

folder_name = "{} {}".format(session_number, title)
try:
    os.makedirs(folder_name)
    with open("{}/Guía de clase - {}.md".format(folder_name, title), "w+") as class_guide:
        class_guide.write(session_template)
except Exception as e:
    print(e)
    print("Esa carpeta ya existe")
