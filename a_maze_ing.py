#! usr/bin/env python3
import sys
from pydantic.types import NonNegativeInt, PositiveInt
"""The visual should clearly show walls, entry, exit, and the solution path.
User interactions must be available, at least for the following tasks:
• Re-generate a new maze and display it.
• Show/Hide a valid shortest path from the entrance to the exit.
• Change maze wall colours.
• Optional: set specific colours to display the “42” pattern.
You can add extra user interactions.""" 

def convert(lst) -> dict:
   res_dict = {}
   for i in range(0, len(lst), 2):
       res_dict[lst[i]] = lst[i + 1]
   return res_dict

def parse_coord(string: str) -> tuple:
    try:
        coords: tuple = tuple()
        for arg in string.split(","):
            coords = coords + (int(arg), )
        if (len(coords) != 2):
            raise ValueError
        return (coords)
    except ValueError:
        raise ValueError("Coordinate non valide")


class Maze:
    WIDTH: PositiveInt
    HEIGHT: PositiveInt
    ENTRY: tuple[NonNegativeInt, NonNegativeInt]
    EXIT: tuple[NonNegativeInt, NonNegativeInt]
    OUTPUT_FILE: str
    PERFECT: bool

    def __init__(self, config: dict):
        need = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}
        for key in config:
            key_caps = str(key).strip()
            if key_caps not in need:
                raise ValueError("invalid configuration key")
        try:
            if (int(config["WIDTH"]) <= 0) | (int(config["HEIGHT"]) <= 0):
                raise ValueError("invalid dimension")
            self.WIDTH = int(config["WIDTH"])
            self.HEIGHT = int(config["HEIGHT"])
            self.ENTRY = parse_coord(str(config["ENTRY"]))
            self.EXIT = parse_coord(str(config["EXIT"]))
            self.OUTPUT_FILE = str(config["OUTPUT_FILE"])
            perfezione = config["PERFECT"]
            if (perfezione == "True"):
                self.PERFECT = True
            elif (perfezione == "False"):
                self.PERFECT = False
            else:
                raise ValueError("Tipo non valido per la chiave: PERFECT")
            print(config)
        except Exception as x:
            print("Errore:", x)




def main():
    if len(sys.argv) != 2:
        print("Error: si usa cosi':\n" 
              f" python3 {sys.argv[0]} config.txt")
        return

    try:
        with open(sys.argv[1], "r") as f:
            config = dict()
            for line in f:
                if "=" not in line:
                    raise ValueError("invalid configuration")
                if (line[0] != "#"):
                    config = config | convert(line.strip().split("="))
            print(f"{config}")

        maze = Maze(config)

    except Exception as x:
        print("Errore:", x)










if __name__ == "__main__":
    main()
