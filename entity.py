from utils import IntVec

class Entity:
    
    def __init__(self, pos: IntVec, depth: int = 0):
        self.pos = pos
        self.depth = depth
    
    def update(self, dt):
        pass
    
    def render(self):
        pass
    
    def events(self, event):
        pass