import pandas as pd
import matplotlib.pyplot as plt

from tests.dir_ops import create_dir_if_not_exists

stock_data_path = "C://Users/SCHOOL/PycharmProjects/stock_analyzer/data/historical_data/RELIANCE.NS.csv"
df = pd.read_csv(stock_data_path)
df= df.set_index(['Date'])
df.index  = pd.to_datetime(df.index)
print(df)


df.plot(y=["Open"])
plt.show()
print()

def get_column_inference(df, directory=None, dtypes=[int, float], column_names=[]):
    '''
    :param df:
    :param directory:
    :param dtypes: column of these
    :return: dictionary of plots
    '''

    numeric_df = df._get_numeric_data()



'''
df["cgo"] = df["Close"] > df["Open"]
df["cgo"].sum() / len(df["cgo"])
'''









