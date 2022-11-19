colors = ['blue', 'green', 'black', 'yellow', 'orange', 'red', 'purple','white', 'brown', 'grey']


def save_file():
    f = open('colors.txt', 'a')
    for color in colors:
        f.write(color + '\n')
    f.close

save_file()