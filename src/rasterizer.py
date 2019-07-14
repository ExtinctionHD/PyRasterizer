from PIL import Image


FULL_HD = (1920, 1080)


def do():
    img = Image.new('RGB', FULL_HD, 'black')
    img.show()


if __name__ == "__main__":
    do()
