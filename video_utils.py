#docs: https://pyav.basswood-io.com/docs/stable

import os
import av # type: ignore
from PIL import Image

from utils import ImageInfo


def extract_frames(input_path: str):
    with av.open(input_path) as container:
        # Signal that we only want to look at keyframes.
        stream = container.streams.video[0]
        #stream.codec_context.skip_frame = "NONKEY"

        for index, frame in enumerate(container.decode(video=0)):
            frame.to_image().save(f"frames/frame-{index:04d}.jpg")


def collect_imgs_to_video(outputPath: str, framesPath:str, framerate, imageInfo: ImageInfo):
    container = av.open(outputPath, mode='w')

    # Add a stream to the container
    stream = container.add_stream('mpeg4', rate=framerate)

    # Set the stream's width, height, and pixel format
    # We assume all images are the same size

    frames = os.listdir(framesPath)

    stream.width = imageInfo.width
    stream.height = imageInfo.height
    stream.pix_fmt = 'yuv420p'

    # Loop through all images and add them to the video
    for img_name in frames:
        img_path = os.path.join(framesPath, img_name)
        
        with Image.open(img_path) as img:
            frame = av.VideoFrame.from_image(img)
            for packet in stream.encode(frame):
                container.mux(packet)

    # Flush the stream
    for packet in stream.encode():
        container.mux(packet)

    # Close the container
    container.close()


if __name__ == "__main__":
    extract_frames("images/input/akira_slide.mp4")