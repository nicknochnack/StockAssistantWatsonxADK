import yfinance as yf 
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission 

@tool(name='get_stock_prices_yf', description='a tool to bring back stock prices by passing through a stock ticker', permission=ToolPermission.ADMIN)
def get_stock_prices_yf(stock_ticker:str): 
    ticker = yf.Ticker(stock_ticker)

    return ticker.history(period='1mo')