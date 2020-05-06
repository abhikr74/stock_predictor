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

def crop_df(df, start_date, end_date):
    from_start_date_df = df[df.index >= start_date]
    to_end_date_df = from_start_date_df[from_start_date_df.index <= end_date]
    return to_end_date_df
    print()

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
        df_new = crop_df(df, start_date, end_date)
        # df_new = df[df.index > start_date]
        # df_new = df[df.index <>> start_date]
        df_new["cgo"] = df_new["Close"] > df_new["Open"]
        probability_cgo = df_new["cgo"].sum() / len(df_new["cgo"])
        top_stocks[stock] = probability_cgo

    return ({k: v for k, v in sorted(top_stocks.items(), key=lambda item: item[1], reverse=True)})

stocks = top_stocks(stocks_list, '01-01-2018', '01-01-2020')
print(stocks)

'''
def func(topXStocks[int], start_date, end_date):
def closing_price_grater_than_opening_price_checker(stock, opening_price, closing_price):
    
    #condition to check opening and closing price for a particular stock
     #check how much and how may times stock is above opening price
    #return

'''