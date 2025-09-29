def equal(position, pixels, cursor):
    posa = (cursor.position[0] + cursor.dir[0], cursor.position[1] + cursor.dir[1])
    posb = position
    
    if (pixels[posa[0], posa[1]] == pixels[posb[0], posb[1]]):
        cursor.move()
        cursor.effect = False
    else:
        while pixels[cursor.position[0], cursor.position[1]][0] != 16:
            cursor.move()
        cursor.move()