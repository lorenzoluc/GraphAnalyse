from functions.isinteger import is_valid_integer
from collections import defaultdict, deque

def IntegerHighway(df):
    for index, row in df.iterrows():
        id_value = row["id"]
        x_value = row["x"]
        y_value = row["y"]
        width_value = row["width"]

        if not (is_valid_integer(id_value) or id_value == "highway"):
            raise ValueError("Invalid format for Id/Type. Expecting an integer id number or 'highway'")
        if not is_valid_integer(x_value)[0]:
            raise ValueError("Invalid format for coordinate X. Expecting an integer or list of integer")
        if not is_valid_integer(y_value)[0]:
            raise ValueError("Invalid format for coordinate Y. Expecting an integer or list of integer")
        if not is_valid_integer(width_value)[0]:
            raise ValueError("Invalid format for width. Expecting an integer")

        row["x"] = is_valid_integer(x_value)[1]
        row["y"] = is_valid_integer(y_value)[1]
        row["width"] = is_valid_integer(width_value)[1]



def contiguous(df):
    spaces = defaultdict(list)

    for _, linha in df.iterrows():
        if is_valid_integer(linha['id']):
            spaces[linha['id']].append({
                'id': linha['id'],
                'x': int(linha['x']),
                'y': int(linha['y'])
            })

    for id_constru, space_constru in spaces.items():
        if not verify_contiguous(space_constru):
            raise Exception(f"The space whit ID {id_constru} IS NOT contiguous.")

def verify_contiguous(space):
    space_set = {(j['x'], j['y']) for j in space}
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS
    visited = set()
    line = deque([(space[0]['x'], space[0]['y'])])
    visited.add((space[0]['x'], space[0]['y']))

    while line:
        x, y = line.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if (nx, ny) in space_set and (nx, ny) not in visited:
                visited.add((nx, ny))
                line.append((nx, ny))




    return len(visited) == len(space_set)