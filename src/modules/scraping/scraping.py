import pandas as pd
import yfinance


def obtain_ticker_history(ticker: str = 'TSLA',
                          start_date: pd.Timestamp = pd.to_datetime('2022-12-31'),
                          time_offset: int = 1500) -> pd.DataFrame:
    """
    Downloads pricing data from yfinance for the ticker required
    :param ticker: a ticker corresponding to the instrument we need
    :param start_date: this will be the date when the transaction happened
    :param time_offset: number of historical days before transaction date to appear in
    the price history
    :return: pd.DataFrame containing pricing data for the ticker
    """
    # Download the data from yfinance
    temp = yfinance.download(ticker, start=start_date + pd.DateOffset(days=-time_offset))
    temp.reset_index(inplace=True)
    return temp
