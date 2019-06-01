import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict



def read_data(f):
    data_ = OrderedDict()
    data = pd.read_csv(f)
    data_["Fuel"] = 1000 * data["FuelC"] / data["Pop"]
    data_["Tax"] = data["Tax"]
    data_["Dlic"] = 1000 * data["Drivers"] / data["Pop"]
    data_["Income"] = data["Income"]
    data_["log(Miles)"] = np.log(data["Miles"])
    df = pd.DataFrame(data_)
    pd.plotting.scatter_matrix(df, marker='o', diagonal='kde')
    plt.show()

if __name__=='__main__':
    f = "fuel2001.csv"
    read_data(f)