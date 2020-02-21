# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# exercise 1
# 打开文本
test = open('constitution.txt').read()
# 生成对象
wc = WordCloud().generate(test)

# 显示词云
# plt.imshow(wc,interpolation="bilinear")
# plt.axis('off')
# plt.show()

# 保存到文件
# wc.to_file('wordcloud_01.png')


# # exercise 2 - 未分词状态
# 中文分词
text2 = open('xyj.txt',encoding='utf-8').read()
wc2 = WordCloud(font_path='Hiragino.ttf',width=800,height=600,mode='RGBA',background_color=None).generate(text2)

#显示词云
# plt.imshow(wc2,interpolation="bilinear")
# plt.axis('off')
# plt.show()

# 保存到文件
# wc2.to_file('wordcloud_02.png')

# exercise 3 分词
import jieba
text3 = ' '.join(jieba.cut(text2))
# print(text3[:100])

# 生成词云对象
wc3 = WordCloud(font_path='Hiragino.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text3)

#显示词云
# plt.imshow(wc3,interpolation="bilinear")
# plt.axis('off')
# plt.show()

# 保存到文件
# wc3.to_file('wordcloud_03.png')

# exercise 4
# 使用蒙版，生成指定形状的词云

