import os
from pathlib import Path

def read_file():
    archivo = Path("..") / "resources" / "matriz.txt"
    print(archivo.resolve())

    with open("../resources/matrices/matriz.txt.", "r") as file:
        print(file.readlines())
    
if __name__ == "__main__":
    read_file()
