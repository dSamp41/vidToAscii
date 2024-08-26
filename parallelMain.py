from functools import partial
import os
import time
from joblib import Parallel, delayed

from coloredTextToImg import assemble_text_colormap
from img_utils import img_to_text #type: ignore
from parsing import text_to_colormap
from stucts import ImageInfo, Info, TextInfo
from video_utils import collect_imgs_to_video, extract_frames, get_size

INPUT_PATH = "images/input"
OUTPUT_PATH = "images/output"
MAPPINGS_PATH = "images/mappings"

FRAMES_FOLDER = "frames"
FRAMES_ASCII_FOLDER = "frames_ascii"


def clear_folder(folder: str) -> None:
    for file in os.listdir(folder):
        os.remove(f"{folder}/{file}")


def main_processing(IMAGE_INFO: ImageInfo, TEXT_INFO: TextInfo, img):
    filename = img.split(".")[0]

    #frame png -> text
    img_to_text(f"{FRAMES_FOLDER}/{img}", f"{MAPPINGS_PATH}/{filename}.txt", IMAGE_INFO, TEXT_INFO)

    #processing
    text_to_colormap(f"{MAPPINGS_PATH}/{filename}.txt", f"{MAPPINGS_PATH}/chars-{filename}.txt", f"{MAPPINGS_PATH}/colors-{filename}.txt")
    
    #overlap text and color        
    assemble_text_colormap(f"{MAPPINGS_PATH}/chars-{filename}.txt", f"{MAPPINGS_PATH}/colors-{filename}.txt", f"{FRAMES_ASCII_FOLDER}/{filename}.png", 15, TEXT_INFO)



if __name__ == "__main__":
    fileName = "evaExplosion"
    VIDEO = f"{INPUT_PATH}/{fileName}.mp4"
    COLS = 500
    
    FRAME_RATE = 24
    (width, height) = get_size(VIDEO) 
    INFO = Info(TextInfo(COLS), ImageInfo(FRAME_RATE, width, height))

    IMAGE_INFO: ImageInfo = INFO.imgInfo
    TEXT_INFO: TextInfo = INFO.txtInfo

    start = time.time()

    try:
        # video -> frames (pngs)
        extract_frames(VIDEO, FRAMES_FOLDER)
        
        # forall frame -> ascii img
        part = partial(main_processing, IMAGE_INFO, TEXT_INFO)
        Parallel(n_jobs=-1)(delayed(part)(img) for img in os.listdir(FRAMES_FOLDER))
        

        # asciis -> video
        collect_imgs_to_video(f"{OUTPUT_PATH}/{fileName}_ascii.mp4", FRAMES_ASCII_FOLDER, IMAGE_INFO)
    except KeyboardInterrupt:
        pass
    finally:
        print("cleaning...")
        #clean-up
        for folder in [FRAMES_FOLDER, FRAMES_ASCII_FOLDER, MAPPINGS_PATH]:
            clear_folder(folder)

    print(f"time: {time.time() - start}s")