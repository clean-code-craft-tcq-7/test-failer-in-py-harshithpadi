
def size(cms):
    if cms < 38:
        return 'S'
    elif cms < 42:
        return 'M'
    else:
        return 'L'

assert(size(37) == 'error')
assert(size(37) == 'S')
assert(size(38) == 'M')
assert(size(40) == 'M')
assert(size(43) == 'L')
print("All is well (maybe!)")
