
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

def barChart():
    x_data = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
    y_data_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9] )
    y_data_2 = [4, 5, 6, 7, 1, 2, 3, 4,9]
    plt.bar(x = x_data, height= y_data_1, label='C语言基础', color='c', alpha=0.8)
    # plt.bar(x=x_data, height = y_data_1)
    plt.legend(loc=[1, 0])
    # plt.legend()
    plt.show()

def muchBarChart():
    x_data = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
    y_data_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    y_data_2 = [4, 5, 6, 7, 1, 2, 3, 4, 9]
    x = np.arange(9)
    width =0.35
    plt.bar( x, y_data_1, width , label='C语言基础', color='c', alpha=1)
    plt.bar( x + width, y_data_2, width, label='B语言基础', color='b', alpha=1)
    plt.xticks( x + width/2, x_data)
    plt.legend(loc=[1, 0])
    plt.show()



def lineAndBarChart():
    x_data = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
    y_data_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    y_data_2 = [4, 6,5 , 7, 1, 2, 3, 4, 9]
    x = np.arange(9)
    width = 0.35
    plt.bar(x, y_data_1, width, label='C语言基础', color='c', alpha=1)
    plt.bar(x + width, y_data_2, width, label='B语言基础', color='b', alpha=1)
    plt.plot(x + width ,y_data_2 )
    plt.xticks(x + width / 2, x_data)
    plt.legend(loc=[1, 0])
    plt.show()


if __name__ == '__main__':
    lineAndBarChart()