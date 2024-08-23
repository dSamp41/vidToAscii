from ascii_magic import AsciiArt

cols = 250
img = AsciiArt.from_image("../imgAscii/images/input/howl.png")
img.to_terminal(columns=cols)
#img.to_file(f"test/{cols}-howl.txt", cols, monochrome=False)

'''
with open("frame-0000.txt", "r") as f:
    txt = f.read()

print(txt)'''