from dataclasses import dataclass, field

@dataclass
class TextInfo:
    textCols: int
    textRows: int


@dataclass
class ImageInfo:
    width: int
    height: int
    width_ratio: int = field(init=False)

    def __post_init__(self):
        self.width_ratio = self.width / self.height


type ImagePath = str
type TextPath = str