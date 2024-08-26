from ascii_magic import AsciiArt #type: ignore
from PIL import Image, ImageFont, ImageDraw
from stucts import ImageInfo, ImagePath, TextPath, TextInfo

def img_to_text(inputPath: ImagePath, outputPath: TextPath, imgInfo: ImageInfo, tInfo: TextInfo) -> None:
    img = AsciiArt.from_image(inputPath)
    img.to_file(path=outputPath, columns=tInfo.textCols, width_ratio=imgInfo.width_ratio)


'''def save_img_to_file(inputPath: str, outputPath: str, fontsize: int, info: TextInfo) -> None:
    with open(inputPath, "r") as f:
        ascii_text: str = f.read()

    img_width = 1920
    img_heigth = fontsize * info.textRows
    img = Image.new('RGB', (img_width, img_heigth), color = (255,255,255))
    fnt = ImageFont.truetype("fonts/Consolas.ttf", fontsize)
    draw = ImageDraw.Draw(img)
    
    draw.text((0,0), ascii_text, font=fnt, fill=(0,0,0))

    img.save(outputPath)'''


if __name__ == "__main__":
    imgInfo = ImageInfo(1920, 1080)

    cols = 300
    rows = int((imgInfo.height * cols) / (imgInfo.width * imgInfo.width_ratio))
    txtInfo = TextInfo(cols, rows)

    img_to_text("images/input/frame-0000.jpg", "test/frame-0000.txt", imgInfo, txtInfo)