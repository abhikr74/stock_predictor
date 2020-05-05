import pandas as pd
from app_properties import ApplicationProperties as props
import os

top_1000_stocks_path = os.path.join(props.data_dir, "top_1000_stocks.csv")
top_1000_stocks = pd.read_csv(top_1000_stocks_path)


