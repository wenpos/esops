import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
from sklearn import linear_model

#线性拟合
def use_X():
    # 周广告播放数量
    x = [1, 3, 2, 1, 3]
    # 周汽车销售数据
    y = [14, 24, 18, 17, 27]
    X = np.mat([[1, 3, 2, 1, 3],[1,1,1,1,1]])
    Y = np.mat(np.array(y)).T
    X= X.T
    B = (X.T * X).I * X.T * Y
    print(B)

def lin():
    # X = [1, 2, 3, 4, 5, 6]
    # Y = [2.5, 3.51, 4.45, 5.52, 6.47, 7.51]
    # 周广告播放数量
    X = [1, 3, 2, 1, 3]
    # 周汽车销售数据
    Y = [14, 24, 18, 17, 27]
    # 一次多项式拟合，相当于线性拟合
    z1 = np.polyfit(X, Y, 1)
    p1 = np.poly1d(z1)
    print(z1)  # [ 1.          1.49333333]
    print(p1)  # 1 x + 1.493

    regr = linear_model.LinearRegression()
    x = np.mat(np.array(X)).T
    y= np.mat(np.array(Y)).T
    regr.fit(x, y)
    print('coefficients(b1,b2...):', regr.coef_)
    print('intercept(b0):', regr.intercept_)

    plt.plot(X, 5*np.array(X)+10)
    #画图--散点图
    plt.scatter(X, Y)

    plt.xticks(())
    plt.yticks(())

    plt.show()


def test():
    X = np.mat([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [41, 45, 51, 52, 59, 62, 69, 72, 78, 80, 90, 92, 98, 103],
                [49, 58, 62, 71, 62, 74, 71, 74, 79, 84, 85, 94, 91, 95]])

    X = X.T
    Y = np.mat([28, 39, 41, 44, 43, 50, 51, 57, 63, 66, 70, 76, 80, 84]).T

    B = (X.T * X).I * X.T * Y
    print(B)

#多元线性回归
def mutli_feature_regression():
    # 定义数据集
    x = np.array([[100, 4, 1, 9.3], [50, 3, 0, 4.8], [100, 4, 1, 8.9],
                  [100, 2, 2, 6.5], [50, 2, 2, 4.2], [80, 2, 1, 6.2],
                  [75, 3, 1, 7.4], [65, 4, 0, 6], [90, 3, 0, 7.6],
                  [100, 4, 1, 9.3], [50, 3, 0, 4.8], [100, 4, 1, 8.9], [100, 2, 2, 6.5]])
    x_trans = []
    for i in range(len(x)):
        x_trans.append({'x1': str(x[i][2])})
    vec = DictVectorizer()
    dummyX = vec.fit_transform(x_trans).toarray()
    x = np.concatenate((x[:, :-2], dummyX[:, :], x[:, -1].reshape(len(x), 1)), axis=1)
    x = x.astype(float)
    X = x[:, :-1]
    Y = x[:, -1]
    print(x, X, Y)

    # 训练数据
    regr = linear_model.LinearRegression()
    regr.fit(X, Y)
    print('coefficients(b1,b2...):', regr.coef_)
    print('intercept(b0):', regr.intercept_)

if __name__ == '__main__':
    # test()
    use_X()
    # lin()
    # mutli_feature_regression()