import pandas as pd


'''
df["cgo"] = df["Close"] > df["Open"]
df["cgo"].sum() / len(df["cgo"])
'''
#Fetching stock details
for index, stock in enumerate(list_of_stocks):
    print("{}. Fetching stock : {}".format(index + 1, stock))
    df = pd.read_csv("C://Users/SCHOOL/PycharmProjects/stock_analyzer/data/historical_data/{}.csv".format(stock))
    # if data is blank
    if df.empty:
        stock = "{}.NS".format(stock)
        data = yf.download(stock, start_date, end_date)

    if data.empty:
        stocks_not_found.append(stock)
    else:
        data.to_csv("C://Users/SCHOOL/PycharmProjects/stock_analyzer/data/historical_data/{}.csv".format(stock))
stock_data_path = "C://Users/SCHOOL/PycharmProjects/stock_analyzer/data/historical_data/RELIANCE.NS.csv"
df = pd.read_csv(stock_data_path)
df= df.set_index(['Date'])
df.index  = pd.to_datetime(df.index)
print(df)

def func(topXStocks[int], start_date, end_date):
def closing_price_grater_than_opening_price_checker(stock, opening_price, closing_price):
    '''
    :param stock: stock id
    :param opening_price:
    :param closing_price:
    :return:
    '''
    #condition to check opening and closing price for a particular stock
     #check how much and how may times stock is above opening price
    #return
