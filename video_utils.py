#docs: https://pyav.basswood-io.com/docs/stable

import os
import av # type: ignore
from PIL import Image

from stucts import ImageInfo


def get_size(path: str) -> tuple[int, int]:
    with av.open(path) as container:
        stream = container.streams.video[0]
        #print(stream.base_rate, stream.frames)

        return (stream.width, stream.height)

if __name__ == "__main__":
    print(get_size("images/input/akira_slide.mp4"))

def extract_frames(input_path: str, outputFolder: str = "frames"):
    with av.open(input_path) as container:
        stream = container.streams.video[0]
        
        # Signal that we only want to look at keyframes.
        #stream.codec_context.skip_frame = "NONKEY"

        for index, frame in enumerate(container.decode(video=0)):
            frame.to_image()\
                .save(f"{outputFolder}/frame-{index:04d}.jpg")


def collect_imgs_to_video(outputPath: str, framesPath:str, imageInfo: ImageInfo):
    with av.open(outputPath, mode='w') as container:
        # Add a stream to the container
        stream = container.add_stream('mpeg4', rate=imageInfo.framerate)

        # Set the stream's width, height, and pixel format (assuming all images are the same size)
        img_size = Image.open(f"{framesPath}/frame-0000.png").size
        stream.width = img_size[0]     #imageInfo.width
        stream.height = img_size[1]     #imageInfo.height
        stream.pix_fmt = 'yuv420p'

        # Loop through all images and add them to the video
        frames = os.listdir(framesPath)
        for img_name in frames:
            img_path = os.path.join(framesPath, img_name)
            
            with Image.open(img_path) as img:
                frame = av.VideoFrame.from_image(img)
                for packet in stream.encode(frame):
                    container.mux(packet)

        # Flush the stream
        for packet in stream.encode():
            container.mux(packet)
            

'''if __name__ == "__main__":
    extract_frames("images/input/akira_slide.mp4")'''