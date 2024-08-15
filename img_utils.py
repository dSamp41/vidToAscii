from ascii_magic import AsciiArt #type: ignore
from PIL import Image, ImageFont, ImageDraw #type: ignore

def img_to_text(inputPath: str, outputPath: str, cols=120) -> None:
    img = AsciiArt.from_image(inputPath)
    img.to_file(path=outputPath, columns=cols, monochrome=True) #TODO: remove monochrome


def save_img_to_file(inputPath: str, outputPath: str) -> None:
    with open(inputPath, "r") as f:
        ascii_text: str = f.read()

    img = Image.new('RGB', (1200, 600), color = (255,255,255))
    fnt = ImageFont.truetype("fonts/Consolas.ttf", 15)
    ImageDraw.Draw(img).text((0,0), ascii_text, font=fnt, fill=(0,0,0))

    img.save(outputPath)