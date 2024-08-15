from ascii_magic import AsciiArt #type: ignore
from img_utils import img_to_text, save_img_to_file #type: ignore

import os

from video_utils import collect_imgs_to_video, extract_frames

INPUT_PATH = "images/input"
OUTPUT_PATH = "images/output"
FRAMES_FOLDER = "frames"

img = AsciiArt.from_image(f"{INPUT_PATH}/akira.jpg")
#img.to_terminal(columns=120, monochrome=True)
#img.to_file(path=f"{OUTPUT_PATH}/akira.txt", columns=120, monochrome=True)


#save_img_to_file(f"{OUTPUT_PATH}/akira.txt", f"{OUTPUT_PATH}/akira.png")

# video -> frames (pngs)
extract_frames("images/input/akira_slide.mp4")

# frame -> ascii img
for img in os.listdir(FRAMES_FOLDER):
    filename = img.split(".")[0]
    img_to_text(f"{FRAMES_FOLDER}/{img}", f"{OUTPUT_PATH}/{filename}.txt")
    save_img_to_file(f"{OUTPUT_PATH}/{filename}.txt", f"{OUTPUT_PATH}/{filename}_ascii.png")

    os.remove(f"{OUTPUT_PATH}/{filename}.txt")


# asciis -> video
collect_imgs_to_video("akira_slide_ascii.mp4", f"{OUTPUT_PATH}")