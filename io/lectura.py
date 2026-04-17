import os
from pathlib import Path

def read_file():
    archivo2 = Path(__file__).parent / ".." / "resources" / "matrices" / "matriz.txt"
    
    try:
        readfile = open(archivo2.resolve(), "r")

        # lo que tengas que hacer con el archivo
        readfile.readlines()

    finally:
        #    hay que cerrar
        readfile.close()

    with open(archivo2.resolve(), "r") as file:
        print(file.readlines())

if __name__ == "__main__":
    read_file()