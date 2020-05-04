import pandas as pd
path_top_1000_stocks="C:/Users/SCHOOL/PycharmProjects/stock_analyzer/data/top_1000_stocks.csv"
top_1000_stocks = pd.read_csv(path_top_1000_stocks)
headers = ["serial_no", "symbol", "company_name", "market_capitalization_in_lacs"]
top_1000_stocks.columns = headers
print(top_1000_stocks.head(5))
print(top_1000_stocks.columns)
print(top_1000_stocks.dtypes)


