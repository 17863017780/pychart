

import matplotlib.pyplot as plt

def scatterCHart():
    plt.scatter(2, 4, s=200)  # 传递一对x和y坐标。它将在指定位置绘制一个点，参数s是设置绘制图形时使用的点的尺寸
    plt.title("Square Numbers", fontsize=24)  # 指定标题，并设置标题字体大小
    plt.xlabel("Value", fontsize=14)  # 指定X坐标轴的标签，并设置标签字体大小
    plt.ylabel("Square of Value", fontsize=14)  # 指定Y坐标轴的标签，并设置标签字体大小
    plt.tick_params(axis='both', labelsize=14)  # 参数axis值为both，代表要设置横纵的刻度标记，标记大小为14
    plt.show()  # 打开matplotlib查看器，并显示绘制的图形

if __name__ == '__main__':
    scatterCHart()