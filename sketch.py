import os
from img_utils import Info, img_to_text, save_img_to_file #type: ignore
from video_utils import collect_imgs_to_video, extract_frames

INPUT_PATH = "images/input"
OUTPUT_PATH = "images/output"
FRAMES_FOLDER = "frames"


def clear_folder(folder: str) -> None:
    for file in os.listdir(folder):
        os.remove(f"{folder}/{file}")


COLUMNS = 200
INFO = Info(200, 51)
if __name__ == "__main__":
    # video -> frames (pngs)
    extract_frames("images/input/akira_slide.mp4")

    # frame -> ascii img
    for img in os.listdir(FRAMES_FOLDER):
        filename = img.split(".")[0]
        img_to_text(f"{FRAMES_FOLDER}/{img}", f"{OUTPUT_PATH}/{filename}.txt", COLUMNS)
        save_img_to_file(f"{OUTPUT_PATH}/{filename}.txt", f"{OUTPUT_PATH}/{filename}_ascii.png", 15, INFO)

        os.remove(f"{OUTPUT_PATH}/{filename}.txt")

    # asciis -> video
    collect_imgs_to_video("akira_slide_ascii.mp4", f"{OUTPUT_PATH}")