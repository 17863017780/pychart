
import  matplotlib.pyplot as plt
from pylab import mpl
# 全局设置字体，解决绘图不支持中文的问题
mpl.rcParams['font.sans-serif'] = ['SimHei']   # 雅黑字体

def aloneLineChart():
    squares = [1, 4, 9, 16, 25]
    x = [1, 2, 3, 4, 5]

    # 设置线宽
    plt.plot(x, squares, linewidth=4)

    # 设置图表标题，并给坐标轴添加标签，字体大小
    plt.title("square of 'x'", fontsize=20)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("x^2", fontsize=12)

    # 设置坐标轴刻度标记的大小
    plt.tick_params(axis='both', labelsize=10)

    plt.show()


def someLineChart():
    x1 = [1, 2, 3, 4, 5]
    y1 = [1, 4, 9, 16, 25]

    x2 = [100, 200, 300, 400, 1000]
    y2 = [10, 20, 30, 40, 100]
    plt.xlabel("哈哈哈", fontsize=12)
    plt.ylabel("XNSDSAHFJSDAF", fontsize=12)
    plt.title("This is a chart demo", fontsize=20)
    # plt.tick_params(axis='both', labelsize=10)
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.show()

def otherLineChart():
    x = ["陈加宏", "张晓东", "张婷婷", "汪传敏", "冯娆"]
    y = [10, 20, 30, 40, 10]
    plt.plot(x, y, linewidth=20 )
    plt.show()


if __name__ == '__main__':
    otherLineChart()
