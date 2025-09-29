if __name__ == "__main__":
    print("loading image module...")
    from PIL import Image

    print("creating a new canvas...")
    canvases = [[0] * 256] * 256
    import functions.canvas as canvas
    #canvas.create((0, 0), canvases)
    canvases[0][0] = Image.open("main.png")

    print("overwriting out.png...")
    canvases[0][0].save("out.png", "PNG")

    print("creating a cursor")
    import cursor as cursorConstructor
    
    cursor = cursorConstructor.Cursor()

    current_canvas = canvases[cursor.canvas[0]][cursor.canvas[1]].load()

    print("sleeping...")
    import time
    time.sleep(1)

    print("DONE!")

    while True:
        cursor.store(current_canvas)
        cursor.execute(current_canvas, canvases)
        cursor.affect(current_canvas)
        cursor.move()

        canvases[cursor.canvas[0]][cursor.canvas[1]].save("out.png", "PNG", compress_level=0)
        print(f"{cursor.position} : {cursor.op}")
        time.sleep(0.5)
