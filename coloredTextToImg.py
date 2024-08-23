from PIL import Image, ImageFont, ImageDraw
from stucts import ImagePath, TextInfo, TextPath

COLORS_CODE = {
    'B': (0, 0, 0), #black
    'r': (255, 0, 0), #red
    'g': (0, 255, 0), #green
    'y': (255, 255, 0), #yellow
    'b': (0, 0, 255), #blue
    'm': (255, 0, 255), #magenta
    'c': (0, 255, 255), #cyan
    'W': (255, 255, 255), #white
    'T': (102, 102, 102),  #transparent
    '\n': 'white'
}

def assemble_text_colormap(charsPath: TextPath, colormapPath: TextPath, outputPath: ImagePath, fontsize: int, info: TextInfo) -> None:
    with open(charsPath, "r") as f:
        ascii_text: str = f.read()

    with open(colormapPath, 'r') as f:
        colormap: str = f.read()
    
    FONT_WIDTH = 8.25 #@15 px fontsize
    
    colormap: list[tuple] = list(map(lambda x: COLORS_CODE[x], "".join(colormap)))

    img_width = int(FONT_WIDTH * info.textCols)
    img_heigth = fontsize * info.textRows
    img = Image.new('RGB', (img_width, img_heigth), color = (10, 10, 10))

    fnt = ImageFont.truetype("fonts/Consolas.ttf", fontsize)
    draw = ImageDraw.Draw(img)
    
    (x_pos, y_pos) = (0, 0)

    for n in range(info.textRows):
        for i in range(info.textCols):
            try:
                index = n*(info.textCols+1) + i   # +1 because of \n column
                toWrite = ascii_text[index]

                x_pos = i * FONT_WIDTH
                draw.text((x_pos, y_pos), toWrite, font=fnt, fill=colormap[index])

                #print(f"{n} row {i} col -> {toWrite}")
            except IndexError:
                break

        x_pos = 0
        y_pos += fontsize
   
    
    img.save(outputPath)
     
      
    '''
    mapping = zip(ascii_text, colormap)
    for index in range(len(mapping)):
        (char, color) = mapping[index]

        x_pos = i * FONT_WIDTH
        draw.text((x_pos, y_pos), char, font=fnt, fill=colormap[index])

        pass
    
    '''

if __name__ == "__main__":
    from parsing import text_to_colormap

    c = 500
    INFO = TextInfo(c, 122)
    filename = f"{c}-howl"

    text_to_colormap(f"test/{filename}.txt", f"test/chars-{filename}.txt", f"test/colors-{filename}.txt")
    assemble_text_colormap(f"test/chars-{filename}.txt", f"test/colors-{filename}.txt", f"test/multicolor-{filename}.png", 15, INFO)