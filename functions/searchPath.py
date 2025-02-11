from classes.GraphObjects import *

def searchPath(obj1,obj2,listCoord,ListWid):
    findpath = []
    prices = []

    for firstpos in range(len(obj1.params)): #for multiple point buildings
        x0 = obj1.params[firstpos][0]
        y0 = obj1.params[firstpos][1]

        if (x0, y0) not in listCoord: #if there's no highway at this point
            continue

        for secondpos in range(len(obj2.params)):
            xf = obj2.params[secondpos][0]
            yf = obj2.params[secondpos][1]

            if (xf, yf) not in listCoord: #if there's no highway at this point
                continue

            if (x0, y0) == (xf, yf): #if it's the same point
                continue

            explored = []

            queue = [[(x0, y0)]]
            valid_paths = []

            while queue:
                path = queue.pop(0)
                node = path[-1]

                if node not in explored:
                    neighbours = []
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if dx != 0 and dy != 0: #dont use diagonal
                                continue
                            new_cord = (node[0] + dx, node[1] + dy)
                            if new_cord in listCoord: #check if there's a highway
                                neighbours.append(new_cord)

                    for neighbour in neighbours:
                        new_path = list(path)
                        new_path.append(neighbour)
                        queue.append(new_path)

                        if neighbour == (xf, yf):
                            findpath.append(new_path)
                            explored.append(neighbour)
                            break

                    explored.append(node)

    if len(findpath) != 0:
        prices = []
        for high in findpath:
            price = 0
            for slicehigh in high:
                index = listCoord.index(slicehigh)
                price += ListWid[index]
            prices.append(price)


    return findpath,prices

