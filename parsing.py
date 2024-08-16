COLORS = {
    '30': 'B', #black
    '31': 'r', #red
    '32': 'g', #green
    '33': 'y', #yellow
    '34': 'b', #blue
    '35': 'm', #magenta
    '36': 'c', #cyan
    '37': 'W', #white
    '90': 'T'  #transparent
}

def process_token(token: str) -> str:
    return COLORS[token[0:2]]


def text_to_colormap(inputPath: str, outputPath: str) -> None:
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

    #token code to color
    processed = []
    for row in tokens:
        processed.append(list(map(process_token, row)))

    with open(outputPath, "a") as f1:    
        for r in processed:
            f1.write("".join(r) + '\n')



if __name__ == "__main__":
    text_to_colormap("frame-0000.txt", "colors-frame-0000.txt")