from stucts import TextPath


COLORS = {
    '30': 'B', #black
    '31': 'r', #red
    '32': 'g', #green
    '33': 'y', #yellow
    '34': 'b', #blue
    '35': 'm', #magenta
    '36': 'c', #cyan
    '37': 'W', #white
    '90': 'T',  #transparent
    '70': 'G',   #grey
    '71': 'M'


}

#TOKEN := <num> + m + <char>
def process_token(token: str) -> str:
    return COLORS[token[0:2]]

def process_char(token: str) -> str:
    return token[3]

def text_to_colormap(inputPath: TextPath, outputTextPath: TextPath, outputColormapPath: TextPath) -> None:
    with open(inputPath, "r") as f:
        txt = f.read()

    #split text into rows
    token_rows = txt.split('\n')

    #remove prefix
    tokens = []
    for i in range(len(token_rows)):
        row = token_rows[i].split("[")
        row.remove('')
        tokens.append(row)

    tokens[-1].remove('39m')

    #print("".join(map(process_char, tokens[20])))

    #token code to color
    processed_chars = []
    processed_tokens = []

    for row in tokens:
        processed_chars.append(map(process_char, row))
        processed_tokens.append(map(process_token, row))

    with open(outputTextPath, "a") as f:
        for r in processed_chars:
            f.write("".join(r) + '\n')

    with open(outputColormapPath, "a") as f:
        for r in processed_tokens:
            f.write("".join(r) + '\n')



if __name__ == "__main__":
    filename = "500-howl.txt"
    text_to_colormap(f"test/{filename}", f"test/chars-{filename}", f"test/colors-{filename}")