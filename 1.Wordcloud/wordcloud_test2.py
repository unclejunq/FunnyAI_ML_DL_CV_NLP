from wordcloud import WordCloud
from wordcloud import ImageColorGenerator # 从Mask中抽取颜色
from PIL import Image  # 读取PNG图片需要用PIL
import numpy as np
import matplotlib.pyplot as plt
import jieba

# 打开文本
text = open('xyj.txt',encoding='utf-8').read()

# 中文分词
text = ' '.join(jieba.cut(text))

# 生成对象
# mask = np.array(Image.open("black_mask.png"))
mask = np.array(Image.open("color_mask.png")) # 打开蒙版并转换成数组

wc = WordCloud(mask=mask, font_path='Hiragino.ttf', width=600, height=500, mode='RGBA',\
               background_color=None).generate(text)
# 从图片中生成颜色
image_colors = ImageColorGenerator(mask) # mask 必须是要有颜色的
wc.recolor(color_func=image_colors)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存到文件
# wc.to_file('wordcloud_4.png')