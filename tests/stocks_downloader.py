import pandas as pd
import yfinance as yf
import os

path_top_1000_stocks="C:/Users/SCHOOL/PycharmProjects/stock_analyzer/data/top_1000_stocks.csv"
top_1000_stocks = pd.read_csv(path_top_1000_stocks)
headers = ["serial_no", "symbol", "company_name", "market_capitalization_in_lacs"]
top_1000_stocks.columns = headers
stocks_list = list(top_1000_stocks['symbol'])

#data = yf.download('RELIANCE.NS','2017-01-01','2020-05-01')
#data.to_csv("ril.csv")


def download_stocks(list_of_stocks, start_date, end_date, directory_to_save):
    stocks_not_found = []
    create_dir_if_not_exists("C://Users/SCHOOL/PycharmProjects/stock_analyzer/data/{}".format(directory_to_save))
    for index, stock in enumerate(list_of_stocks):
        print("{}. Downloading stock : {}".format(index+1, stock))
        data = yf.download(stock, start_date, end_date)
        # if data is blank
        if data.empty:
            stock = "{}.NS".format(stock)
            data = yf.download(stock, start_date, end_date)

        if data.empty:
            stocks_not_found.append(stock)
        else:
            data.to_csv("C://Users/SCHOOL/PycharmProjects/stock_analyzer/data/historical_data/{}.csv".format(stock))

    return stocks_not_found

# Function to create directory
def create_dir_if_not_exists(path):
   if not os.path.exists(path):
       os.mkdir(path)

stocks_not_found = download_stocks(stocks_list, '2018-01-01', '2020-05-01', "historical_data")
print(stocks_not_found)

