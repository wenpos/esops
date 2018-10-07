import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import radviz
sns.set(style="white", color_codes=True)

iris = pd.read_csv("./Iris.csv")
print(iris.head())
print(iris["Species"].value_counts())
#散点图
iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")
#散点图+柱状图
sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=5)
#散点图，加标签，用不同颜色区分
sns.FacetGrid(iris, hue="Species", size=5) \
   .map(plt.scatter, "SepalLengthCm", "SepalWidthCm") \
   .add_legend()
#箱型图
sns.boxplot(x="Species", y="PetalLengthCm", data=iris)

#箱型图
ax = sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
ax = sns.stripplot(x="Species", y="PetalLengthCm", data=iris, jitter=True, edgecolor="gray")

#核密度图
sns.FacetGrid(iris, hue="Species", size=6) \
   .map(sns.kdeplot, "PetalLengthCm") \
   .add_legend()
#多变量图
sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3)

#弹力图
radviz(iris.drop("Id", axis=1), "Species")
plt.show()
