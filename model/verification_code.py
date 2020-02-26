from PIL import Image

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random


def validate_picture(width, height, characters, front_color, background_color  ):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345789'
    im = Image.new('RGB', (width, height), front_color)
    # font = ImageFont.truetype(r'D:\ProgramData\Miniconda3\envs\python3.6\Library\lib\fonts\VeraSeBd.ttf', 30)
    draw = ImageDraw.Draw(im)
    str = ''
    for item in range(5):
        text = random.choice(characters)
        str += text
        draw.text((5 + random.randint(4, 7) + 20 * item, 5 + random.randint(3, 7)), text=text, fill=background_color)

    """
    for num in range(8):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, heighth / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(heighth / 2, heighth)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)
    """

    im = im.filter(ImageFilter.FIND_EDGES)
    # im.show()
    return im, str


# 返回验证码图片和验证码字符串
class verification_code:
    def __init__(self, width, height, front_color='white', background_color="black"):
        self.width = width
        self.height = height
        self.characters = []
        self.style=None
        self.front_color = front_color
        self.background_color = background_color

    def draw(self):
        img, content = None, None
        if self.style is None:
            # 对生成图片再次渲染
            characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345789'
            img,content = validate_picture(width=self.width, height=self.height, characters=characters, \
                             background_color=self.background_color, front_color=self.front_color )
        return  img, content

if __name__ == "__main__":
    vc = verification_code(200,200)
    img, content = vc.draw()
    # img.show()