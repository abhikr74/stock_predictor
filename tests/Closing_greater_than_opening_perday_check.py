import pandas as pd
import os
import matplotlib.pyplot as plt


'''
df["cgo"] = df["Close"] > df["Open"]
df["cgo"].sum() / len(df["cgo"])
'''

path_top_1000_stocks="C:/Users/SCHOOL/PycharmProjects/stock_analyzer/data/top_1000_stocks.csv"
top_1000_stocks = pd.read_csv(path_top_1000_stocks)
headers = ["serial_no", "symbol", "company_name", "market_capitalization_in_lacs"]
top_1000_stocks.columns = headers
stocks_list = list(top_1000_stocks['symbol'])

#Fetching stock details

def top_stocks(list_of_stocks, start_date=None, end_date=None):
    top_stocks = {}
    stocks_not_found = []
    for stock in list_of_stocks:

        stock_data_path = "C://Users/SCHOOL/PycharmProjects/stock_analyzer/data/historical_data/{}.csv".format(stock)

        if not os.path.exists(stock_data_path):
            stock = "{}.NS".format(stock)
            stock_data_path = "C://Users/SCHOOL/PycharmProjects/stock_analyzer/data/historical_data/{}.csv".format(stock)

        if not os.path.exists(stock_data_path):
            stocks_not_found.append(stock)
            continue

        else:
            stock_data_path = "C://Users/SCHOOL/PycharmProjects/stock_analyzer/data/historical_data/{}.csv".format(stock)

        df = pd.read_csv(stock_data_path)
        df = df.set_index(['Date'])
        df.index = pd.to_datetime(df.index)
        df["cgo"] = df["Close"] > df["Open"]
        probability_cgo = df["cgo"].sum() / len(df["cgo"])
        top_stocks[stock] = probability_cgo

    return ({k: v for k, v in sorted(top_stocks.items(), key=lambda item: item[1], reverse=True)})

stocks = top_stocks(stocks_list)
print(stocks)
'''
def func(topXStocks[int], start_date, end_date):
def closing_price_grater_than_opening_price_checker(stock, opening_price, closing_price):
    
    #condition to check opening and closing price for a particular stock
     #check how much and how may times stock is above opening price
    #return

'''