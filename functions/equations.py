def add(position, pixels, cursor):
    a = pixels[cursor.position[0] + cursor.dir[0], cursor.position[1] + cursor.dir[1]]
    b = pixels[cursor.position[0] + cursor.dir[0] * 2, cursor.position[1] + cursor.dir[1] * 2]

    c = (min(a[0] + b[0], 255), min(a[1] + b[1], 255), min(a[2] + b[2], 255))
    pixels[position[0], position[1]] = c