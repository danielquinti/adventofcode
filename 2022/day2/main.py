results = [
    [3, 0, 6],
    [6, 3, 0],
    [0, 6, 3]
]

def get_score(my_shape,oponent_shape):
        my_shape_score = ord(my_shape)-64
        print(f'My shape: {}')
        oponent_shape_score = ord(oponent_shape)-87
        return my_shape_score + results[my_shape_score-1][oponent_shape_score-1]
import os
with open(os.path.join(os.getcwd(), "input.txt")) as f:
    print(sum([get_score(line[0],line[2]) for line in f]))

