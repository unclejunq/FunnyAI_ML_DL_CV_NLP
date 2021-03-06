# 控制每一个词的颜色
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator # 从Mask中抽取颜色
from PIL import Image  # 读取PNG图片需要用PIL
import numpy as np
import matplotlib.pyplot as plt
import jieba
import random

# 打开文本
text = open('xyj.txt',encoding='utf-8').read()

# 中文分词
text = ' '.join(jieba.cut(text))

# 颜色函数
# https://www.w3.org/wiki/CSS3/Color/HSL HSL配色方案参考
def ram_color(word, font_size, position, orientation, font_path, random_state):
    '''
    可以个性化再次设置，精细控制
    :param word:
    :param font_size:
    :param position:
    :param orientation:
    :param font_path:
    :param random_state:
    :return:
    '''
    s = 'hsl(0, %d%%, %d%%)' % (random.randint(60,80), random.randint(60,80))
    # hsl, 色相，饱和度，亮度
    print(s)
    return s
# 生成对象
# mask = np.array(Image.open("black_mask.png"))
mask = np.array(Image.open("color_mask.png")) # 打开蒙版并转换成数组

wc = WordCloud(color_func=ram_color,mask=mask, font_path='Hiragino.ttf', width=600, height=500, mode='RGBA',\
               background_color=None).generate(text)
# 从图片中生成颜色
image_colors = ImageColorGenerator(mask) # mask 必须是要有颜色的
# wc.recolor(color_func=image_colors)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存到文件
# wc.to_file('wordcloud_4.png')