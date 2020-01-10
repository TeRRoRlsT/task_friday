"""
Python Paint v1.0

"""
from sys import stderr

INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'


def create_canvas(_, w, h):
    """
    Function of creating canvas.

    :param w: raw string value of width
    :param h: raw string value of height
    """
    canvas = [[' '] * (int(w) + 2) for _ in range(int(h) + 2)]
    for j in range(0, len(canvas[0])):
        canvas[0][j] = '-'
        canvas[len(canvas) - 1][j] = '-'
    for j in range(1, len(canvas) - 1):
        canvas[j][0] = '|'
        canvas[j][len(canvas[0]) - 1] = '|'

    return canvas


def draw_rectangle(canvas, _x1, _y1, _x2, _y2):
    """
    Function of drawing rectangle.

    :param canvas: canvas field for drawing rectangle
    :param _x1: raw string value X1
    :param _y1: raw string value Y1
    :param _x2: raw string value X2
    :param _y2: raw string value Y2
    """
    if canvas is not None:
        x1, y1 = int(_x1), int(_y1)
        x2, y2 = int(_x2), int(_y2)

        for el in range(x1, x2 + 1):
            if el in range(1, len(canvas[0]) - 1):
                if y1 in range(1, len(canvas) - 1):
                    canvas[y1][el] = 'x'
                if y2 in range(1, len(canvas) - 1):
                    canvas[y2][el] = 'x'

        for el in range(y1, y2 + 1):
            if el in range(1, len(canvas) - 1):
                if x1 in range(1, len(canvas[0]) - 1):
                    canvas[el][x1] = 'x'
                if x2 in range(1, len(canvas[0]) - 1):
                    canvas[el][x2] = 'x'

    return canvas


def draw_line(canvas, _x1, _y1, _x2, _y2):
    """
    Function of drawing line.

    :param canvas: canvas field for drawing line
    :param _x1: raw string value X1
    :param _y1: raw string value Y1
    :param _x2: raw string value X2
    :param _y2: raw string value Y2
    """
    if canvas is not None:
        x1, y1, x2, y2 = int(_x1), int(_y1), int(_x2), int(_y2)

        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)

        if x1 == x2:
            for iy in range(max(y1, 1), min(y2 + 1, len(canvas) - 1)):
                canvas[iy][x1] = 'x'
        elif y1 == y2:
            for ix in range(max(x1, 0), min(x2 + 1, len(canvas[0]) - 1)):
                canvas[y1][ix] = 'x'

    return canvas


def brush(canvas, _x, _y, c):
    """
    Recursive function of Bucket Fill.

    :param canvas: canvas field for brush
    :param _x: raw string value X
    :param _y: raw string value Y
    :param c: char color for brush
    """
    if canvas is not None:
        x, y = int(_x), int(_y)

        if canvas[y][x] == ' ':
            canvas[y][x] = c
            if x + 1 in range(1, len(canvas[0]) - 1) and canvas[y][x + 1] == ' ':
                brush(canvas, x + 1, y, c)
            if x - 1 in range(1, len(canvas[0]) - 1) and canvas[y][x - 1] == ' ':
                brush(canvas, x - 1, y, c)
            if y + 1 in range(1, len(canvas) - 1) and canvas[y + 1][x] == ' ':
                brush(canvas, x, y + 1, c)
            if y - 1 in range(1, len(canvas) - 1) and canvas[y - 1][x] == ' ':
                brush(canvas, x, y - 1, c)

    return canvas


def main():
    rules = {'C': create_canvas, 'R': draw_rectangle, 'L': draw_line, 'B': brush}

    with open(INPUT_FILE) as fin:
        commands = [line.split() for line in fin.readlines()]

    canvas = None
    open(OUTPUT_FILE, 'w').close()

    for command in commands:
        canvas = rules[command[0]](canvas, *command[1:])
        with open(OUTPUT_FILE, 'a') as fout:
            for elem in canvas:
                fout.write(''.join(elem) + '\n')


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(f'Error: {err}', file=stderr)
