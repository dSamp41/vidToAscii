from ascii_magic import AsciiArt

img = AsciiArt.from_image("images/input/frame-0000.jpg")
img.to_terminal(columns=200)
#img.to_file("frame-0000.txt", 200, monochrome=False)

'''
with open("frame-0000.txt", "r") as f:
    txt = f.read()

print(txt)'''