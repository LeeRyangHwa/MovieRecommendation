from matplotlib import pyplot as plt
import numpy as np
import matplotlib
from matplotlib import font_manager, rc
import platform
def graphDraw(review, title):
    #print("graphDraw",review)
    x =[]
    y=[]

    for content in review:
        x.append(content[0])
        y.append(content[1])

    if platform.system() == 'Windows':
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    matplotlib.rcParams['axes.unicode_minus'] = False

    num = np.arange(len(x))

    plt.xticks(num, x)
    plt.bar(num, y)

    plt.xlabel('Word')
    plt.ylabel('Count')

    plt.title(title + '(리뷰 키워드)')

    plt.show()