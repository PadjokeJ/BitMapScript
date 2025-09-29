def jump(to: tuple, cursor):
    cursor.position = to
    cursor.effect = False
    cursor.tick = False