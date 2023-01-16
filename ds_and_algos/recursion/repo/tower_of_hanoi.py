

def tower_of_hanoi(n, src, dst, aux):
    if n == 1:
        print('move disk {} from {} to {}'.format(n, src, dst))
    else:
        tower_of_hanoi(n-1, src, aux, dst)
        print('/ move disk {} from {} to {}'.format(n, src, dst))
        tower_of_hanoi(n-1, aux, dst, src)

tower_of_hanoi(4, 'src', 'dst', 'aux')