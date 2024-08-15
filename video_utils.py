#docs: https://pyav.basswood-io.com/docs/stable

import av # type: ignore
import av.datasets # type: ignore

content = av.datasets.curated("pexels/time-lapse-video-of-night-sky-857195.mp4")

def extract_frames(input_path: str):
    with av.open(input_path) as container:
        # Signal that we only want to look at keyframes.
        stream = container.streams.video[0]
        #stream.codec_context.skip_frame = "NONKEY"

        for index, frame in enumerate(container.decode(video=0)):
            frame.to_image().save(f"frames/frame-{index:04d}.jpg")