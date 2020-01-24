from entity import Entity

class EntityManager:

    def __init__(self):
        self.entities = []

    def add(self, entity):
        if isinstance(entity, Entity):
            self.entities.append(entity)
        else:
            raise Exception("Can only add Entity to list.")

    def remove(self, entity):
        self.entities.remove(entity)
    
    def sort(self):
        self.entities.sort(key=lambda e: e.depth, reverse=True)

entity_manager = EntityManager()