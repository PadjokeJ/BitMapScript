def str_to_rgb(strng):
    rstr = strng[0:2]
    gstr = strng[2:4]
    bstr = strng[4:6]

    r = int(rstr, 16)
    g = int(gstr, 16)
    b = int(bstr, 16)

    print((r, g, b))

    return (r, g, b)

if __name__ == "__main__":
    from PIL import Image

    img = Image.new("RGB", (256, 256))
    pixels = img.load()

    lines = []
    with open("main.bms", 'r') as f:
        lines = f.readlines()

    fileindex = 0

    for y in range(256):
        for x in range(256):
            try:
                if lines[fileindex].startswith("endl"):
                    print("break")
                    break
                pixels[x, y] = str_to_rgb(lines[fileindex])
                print(f"{x}, {y}")
            except Exception as e: 
                ...
            fileindex += 1
        fileindex += 1


    img.save("main.png", "PNG")