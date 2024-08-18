import os
from coloredTextToImg import assemble_text_colormap
from img_utils import img_to_text #type: ignore
from parsing import text_to_colormap
from utils import ImageInfo, TextInfo
from video_utils import collect_imgs_to_video, extract_frames

INPUT_PATH = "images/input"
OUTPUT_PATH = "images/output"
MAPPINGS_PATH = "images/mappings"

FRAMES_FOLDER = "frames"
FRAMES_ASCII_FOLDER = "frames_ascii"


def clear_folder(folder: str) -> None:
    for file in os.listdir(folder):
        os.remove(f"{folder}/{file}")


if __name__ == "__main__":
    IMAGE_INFO = ImageInfo(1920, 1080)

    COLS = 700
    ROWS = int((IMAGE_INFO.height * COLS) / (IMAGE_INFO.width * IMAGE_INFO.width_ratio))
    TEXT_INFO = TextInfo(COLS, ROWS)

    # video -> frames (pngs)
    extract_frames("images/input/akira_slide.mp4")

    # frame -> ascii img
    for img in os.listdir(FRAMES_FOLDER):
        filename = img.split(".")[0]

        #frame png -> text
        img_to_text(f"{FRAMES_FOLDER}/{img}", f"{MAPPINGS_PATH}/{filename}.txt", IMAGE_INFO, TEXT_INFO)

        #processing
        text_to_colormap(f"{MAPPINGS_PATH}/{filename}.txt", f"{MAPPINGS_PATH}/chars-{filename}.txt", f"{MAPPINGS_PATH}/colors-{filename}.txt")
        
        #overlap text and color        
        assemble_text_colormap(f"{MAPPINGS_PATH}/chars-{filename}.txt", f"{MAPPINGS_PATH}/colors-{filename}.txt", f"{FRAMES_ASCII_FOLDER}/{filename}.png", 15, TEXT_INFO)

    # asciis -> video
    collect_imgs_to_video("akira_slide_ascii.mp4", FRAMES_ASCII_FOLDER, 24, IMAGE_INFO)

#clean-up
for folder in [FRAMES_FOLDER, FRAMES_ASCII_FOLDER, MAPPINGS_PATH]:
    clear_folder(folder)