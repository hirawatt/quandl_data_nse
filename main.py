import quandl
from dotenv import load_dotenv
import os

load_dotenv()
# add quandl_api_key='<api key>' to .env file
quandl.ApiConfig.api_key = os.getenv('quandl_api_key')

portfolio_tickers = ['ADANIGREEN', 'CDSL', 'HTMEDIA', 'IEX', 'SASTASUNDR', 'TEJASNET']

for i in range(6):
    tic = 'NSE/' + str(portfolio_tickers[i])
    print(tic)
    print(quandl.get(tic, column_index=1))
