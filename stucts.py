from dataclasses import dataclass, field

@dataclass
class TextInfo:
    textCols: int
    textRows: int = 0


@dataclass
class ImageInfo:
    width: int
    height: int
    width_ratio: int = field(init=False)

    def __post_init__(self):
        self.width_ratio = self.width / self.height

@dataclass
class Info:
    txtInfo: TextInfo
    imgInfo: ImageInfo

    def __post_init__(self):
        ROWS = int((self.imgInfo.height * self.txtInfo.textCols) / (self.imgInfo.width * self.imgInfo.width_ratio))
        self.txtInfo.textRows = ROWS



type ImagePath = str
type TextPath = str