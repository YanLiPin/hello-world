"""
Simple linear regression by sklearn,
data from Forbes which in Applied Linear Regression.
"""
import pandas as pd
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
import numpy as np


class HandlerForbes(object):

    def __init__(self, fname):
        self.fname = fname

    # read .csv file
    def handle_file(self):
        data = pd.read_csv(self.fname)
        return data

    # simple linear regression using sklearn
    def linear_regression(self):
        regressor = np.asarray(self.handle_file()["bp"]).reshape((-1, 1))
        predictor = np.asarray(self.handle_file()["lpres"])
        model = LinearRegression().fit(regressor, predictor)
        return model.intercept_, model.coef_

    # original data scatter plot & fit linear line
    def plot_scatter(self):
        x = self.handle_file()["bp"]
        y = self.handle_file()["lpres"]
        i = self.linear_regression()[0]
        s = self.linear_regression()[1]
        plt.scatter(x, y)
        plt.plot(x, i + s * x, "r")
        plt.xlabel("bp")
        plt.ylabel("lpres")
        plt.show()


if __name__=='__main__':
    #f = "/home/yanlp/workspace/alr4data/Forbes.csv"
    f = "Forbes.csv"
    obj = HandlerForbes(f)
    obj.plot_scatter()