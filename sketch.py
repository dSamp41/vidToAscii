from ascii_magic import AsciiArt #type: ignore
from utils import save_img_to_file #type: ignore

INPUT_PATH = "images/input"
OUTPUT_PATH = "images/output"

img = AsciiArt.from_image(f"{INPUT_PATH}/akira.jpg")
#img.to_terminal(columns=120, monochrome=True)
#img.to_file(path=f"{OUTPUT_PATH}/akira.txt", columns=120, monochrome=True)


save_img_to_file(f"{OUTPUT_PATH}/akira.txt", f"{OUTPUT_PATH}/akira.png")
