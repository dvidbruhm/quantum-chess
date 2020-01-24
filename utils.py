from dataclasses import dataclass

@dataclass
class IntVec:
    x: int
    y: int

    def to_tuple(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return IntVec(self.x + other.x, self.y + other.y)

def get_inverse_color(color):
    return "black" if color == "white" else "white"