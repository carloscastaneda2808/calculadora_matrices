import os
from pathlib import Path

def read_file():
    archivo = Path(__file__).parent / ".." / "resources" / "matrices" / "matriz.txt"

    with open(archivo.resolve(), "r") as file:
        print(file.readlines())

if __name__ == "__main__":
    read_file()