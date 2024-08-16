from PIL import Image, ImageFont, ImageDraw
from img_utils import Info #type: ignore

COLORS_CODE = {
    'B': (0, 0, 0), #black
    'r': (255, 0, 0), #red
    'g': (0, 255, 0), #green
    'y': (255, 255, 0), #yellow
    'b': (0, 0, 255), #blue
    'm': (255, 0, 255), #magenta
    'c': (0, 255, 255), #cyan
    'W': (255, 255, 255), #white
    'T': "white",  #transparent
    '\n': 'white'
}

#TODO: \n is problematic
def save_img_to_file(inputPath: str, colormapPath: str, outputPath: str, fontsize: int, info: Info) -> None:
    with open(inputPath, "r") as f:
        ascii_text: str = f.read()

    print(ascii_text[200] == '\n')

    with open(colormapPath, 'r') as f:
        colormap: str = f.read()
    
    #colormap: list[str] = colormap.split('\n')
    
    colormap: list[tuple] = list(map(lambda x: COLORS_CODE[x], "".join(colormap)))

    img_width = 1920
    img_heigth = fontsize * info.textRows
    img = Image.new('RGB', (img_width, img_heigth), color = "black")
    fnt = ImageFont.truetype("fonts/Consolas.ttf", fontsize)
    draw = ImageDraw.Draw(img)
    
    (x_pos, y_pos) = (0, 0)

    for n in range(info.textRows):
        for i in range(info.textCols + 1):
            index = n*info.textCols + i
            toWrite = ascii_text[index]

            x_pos = i * 8.25
            draw.text((x_pos, y_pos), toWrite, font=fnt, fill=colormap[index])

            #print(f"{n} row {i} col -> {toWrite}")

        x_pos = 0
        y_pos += fontsize


    img.save(outputPath)
    

if __name__ == "__main__":
    INFO = Info(200, 51)
    save_img_to_file("monochrome-frame-0000.txt", "colors-frame-0000.txt", "multicolor-test.png", 15, INFO)