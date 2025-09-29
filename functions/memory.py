def write(position, pixels, cursor):
    read(cursor.position, pixels, cursor)
    pixels[position[0], position[1]] = (cursor.op, cursor.mem[0], cursor.mem[1])

def read(position, pixels, cursor):
    pixel = pixels[position[0] + cursor.dir[0], position[1] + cursor.dir[1]]
    cursor.mem = (pixel[1], pixel[2])
    cursor.op = pixel[0]