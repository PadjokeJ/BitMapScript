from PIL import Image

def create(id_tuple: tuple, image_memory: list):
    image_memory[id_tuple[0]][id_tuple[1]] = Image.new(mode="RGB", size=(256, 256))
