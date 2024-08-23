from dataclasses import dataclass
from PIL import Image

type ColorName = str
type ColorSymbol = str
type RGB = tuple[int, int, int]

@dataclass
class Color:
    name: ColorName
    symbol: ColorSymbol
    rgb: RGB

type Palette = list[Color]

palette: Palette = [
    Color("black", 'B', (0, 0, 0)),
    Color("red", 'r', (255, 0, 0)),
    Color("green", 'g', (0, 255, 0)),
    Color("yellow", 'y', (255, 255, 0)),
    Color("blue", 'b', (0, 0, 255)),
    Color("magenta", 'm', (255, 0, 255)),
    Color("cyan", 'c', (0, 255, 255)),
    Color("white", 'W', (255, 255, 255)),
    Color("pink", "p", (255, 192, 203)),
    #Color("transparent", 'T', (102, 102, 102))
]

def L2_dist(c1: RGB, c2: RGB) -> float:
    res = 0
    
    for i in range(len(c1)):
        res += (c1[i] - c2[i]) ** 2

    return res ** .5

def remap(oldImg: Image.Image, palette: Palette) -> Image.Image:
    (width, height) = oldImg.size
    newImg = Image.new("RGB", oldImg.size)

    for x in range(width):
        for y in range(height):
            oldPixel = oldImg.getpixel((x, y))

            distances = [None] * len(palette)
            for i in range(len(palette)):
                distances[i] = L2_dist(oldPixel, palette[i].rgb)

            nearestColorIndex = distances.index(min(distances))
            newPixel = palette[nearestColorIndex].rgb

            newImg.putpixel((x, y), newPixel)

    return newImg


if __name__ == "__main__":
    image = "images/input/alt-frame-0000.jpg"
    img = Image.open(image)

    newImg = remap(img, palette)
    newImg = newImg.quantize(len(palette))
    newImg.save("img_test/newImg.png")

    for col in palette:
        PINK = (193, 149, 122)
        
        print(f"vs {col.name}: {L2_dist(PINK, col.rgb)}")