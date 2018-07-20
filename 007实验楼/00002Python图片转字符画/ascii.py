from PIL import Image
import argparse

parser = argparse.ArgumentParser()
# 命令行输入参数处理
parser.add_argument('file')
# 输入文件
parser.add_argument('-o', '--output')
# 输出文件
parser.add_argument('--width', type=int, default=100)
# 定义字符画宽度
parser.add_argument('--height', type=int, default=100)
# 定义字符画高度
args = parser.parse_args()
# 获取参数
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")


# 定义字符
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]

if __name__ == "__main__":
    im = Image.open(IMG)
    im = im.resize(
        (WIDTH, HEIGHT), Image.NEAREST
    )
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt+=get_char(*im.getpixel((j,i)))
        txt+='\n'
    print(txt)
    #输出字符画到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)