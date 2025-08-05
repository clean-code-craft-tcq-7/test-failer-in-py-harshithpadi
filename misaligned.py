def color_index_to_pair(x,y):
    return x*5+ y + 1

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(color_index_to_pair(0,0) == 1)
assert(color_index_to_pair(0,1) == 2)
assert(color_index_to_pair(1,0) == 6)
assert(color_index_to_pair(4,4) == 25)
assert(result == 25)
print("All is well (maybe!)")

