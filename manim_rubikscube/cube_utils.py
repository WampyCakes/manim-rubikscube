from manim.constants import *

def get_axis_from_face(face):
    if face == "F" or face == "B":
        return X_AXIS
    elif face == "U" or face == "D":
        return Z_AXIS
    else:
        return Y_AXIS

def get_direction_from_face(face):
    #Clockwise/counterclockwise for each face. UP goes cw?
    return

def get_type_of_cubie(dim, position):
    if (position[1] == 0 or position[1] == dim-1) and (position[2] == 0 or position[2] == dim-1):
        return "corner"
    elif position[1] == 0 or position[1] == dim-1:
        return "edge"
    else:
        return "center"

#DOWN = IN
#OUT = RIGHT
#LEFT = UP
#UP = OUT
#RIGHT = DOWN
#IN = LEFT
def get_faces_of_cubie(dim, position):
    dim = dim-1
    try:
        faces = {
            #Front corners
            (0, 0, 0): [LEFT, DOWN, IN],
            (0, 0, dim): [LEFT, DOWN, OUT],
            (0, dim, 0): [LEFT, UP, IN],
            (0, dim, dim): [LEFT, UP, OUT],
            #Back corners
            (dim, 0, 0): [RIGHT, DOWN, IN],
            (dim, 0, dim): [RIGHT, DOWN, OUT],
            (dim, dim, 0): [RIGHT, UP, IN],
            (dim, dim, dim): [RIGHT, UP, OUT],
        }
        return faces[position]
    except:
        x = position[0]
        y = position[1]
        z = position[2]

        if x == 0:
            if y == 0:
                return [DOWN, LEFT]
            elif y == dim:
                return [UP, LEFT]
            else:
                if z == 0:
                    return [IN, LEFT]
                elif z == dim:
                    return [OUT, LEFT]
                else:
                    return [LEFT]
        elif x == dim:
            if y == 0:
                return [DOWN, RIGHT]
            elif y == dim:
                return [UP, RIGHT]
            else:
                if z == 0:
                    return [IN, RIGHT]
                elif z == dim:
                    return [OUT, RIGHT]
                else:
                    return [RIGHT]
        else:
            if y == 0:
                if z == 0:
                    return [IN, DOWN]
                elif z == dim:
                    return [OUT, DOWN]
                else:
                    return [DOWN]
            elif y == dim:
                if z == 0:
                    return [IN, UP]
                elif z == dim:
                    return [OUT, UP]
                else:
                    return [UP]
            else:
                if z == 0:
                    return [IN]
                elif z == dim:
                    return [OUT]
                else:
                    return []