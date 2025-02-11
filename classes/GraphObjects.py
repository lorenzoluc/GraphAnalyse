from functions.isinteger import is_valid_integer
from functions.searchPath import *

class GraphElements:
    def __init__(self, typology, params):
        self.typology = typology
        self.params = params
        self.color = ""

    def __repr__(self):
        return f"GraphElement(typology={self.typology}, params={self.params})"

class Building(GraphElements):
    def __init__(self, typology, params):
        super().__init__(typology, params)
        self.color = 'red'

    def __repr__(self):
        return f"Building(id={self.typology}, params={self.params})"

    def distanceTwoBuildings(self,other,listCoord,ListWid): #gets the shortest path
        paths, distance = searchPath(self,other,listCoord,ListWid)

        if len(paths) == 0:
            print("So sorry, but a connecting path doesn't exist :(")
            return
        else:
            print("At least one connection path between those building exists")
            for i in range(len(paths)):
                print(f"Ex: Path {i + 1}: {paths[i]} has a value of {distance[i]}")

        return

class Warehouse(Building):
    def __init__(self, typology, params):
        super().__init__(typology, params)
        self.color = 'blue'

    def __repr__(self):
        return f"Warehouse(id={self.typology}, params={self.params})"

class Highway(GraphElements):
    def __repr__(self):
        return f"Highway(typology={self.typology}, params={self.params})"

    def pathstops(self):
        self.coord = []
        self.wid = []

        if isinstance(self.params[0],tuple):
            self.coord = [(x,self.params[1]) for x in range(self.params[0][0],self.params[0][1]+1)]
        elif isinstance(self.params[1],tuple):
            self.coord = [(self.params[0],y) for y in range(self.params[1][0],self.params[1][1]+1)]

        self.wid = [self.params[2]] * len(self.coord)
        return self.coord, self.wid #ex: [(92,100),(93,100)] and [1,1]

class GraphFactory:
    @staticmethod
    def create_element(dic):
        classesCreated = []
        for key, value in dic.items():
            if is_valid_integer(key):
                # let's assume that the rule to determine if it's a warehouse is if the id ends with the number 2
                warehouseCheck = int(key) % 10
                if warehouseCheck == 2:
                    classesCreated.append(Warehouse(key, value))
                else:
                    classesCreated.append(Building(key, value))
            else:
                for subvalue in value:
                    classesCreated.append(Highway(key, subvalue))
        return classesCreated #ex: [warehouse1,building1,highway1,highway2...]