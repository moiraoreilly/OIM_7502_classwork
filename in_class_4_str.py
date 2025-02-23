import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb  # optional to set plot theme
import yfinance as yf
sb.set_theme()  # optional to set plot theme

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())


class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        """method that downloads data and stores in a DataFrame
           uncomment the code below wich should be the final two lines 
           of your method"""
        symbol = input("Enter a stock symbol to get data on: ")

        start = input("Enter a start date in the format YYYY-MM-DD: ")
        if start == "":
            start = DEFAULT_START
        else:
            start = start
        end = input("Enter an end date in the format YYYY-MM-DD: ")
        if end == "":
            end = DEFAULT_END
        else:
            end = end

        data = yf.download(symbol, start=start, end=end)
        df = pd.DataFrame(data)

        self.data = self.calc_returns(df)
        return self.data

    def calc_returns(self, df):
        """method that adds change and return columns to data"""
        df = df.assign(Change=df['Close'].diff(), Instant_Return=np.log(df['Close']).diff().round(4))
        return df

    def plot_return_dist(self):
        """method that plots instantaneous returns as histogram"""
        plt.hist(self.data['Instant_Return'], bins=50)
        plt.show()

    def plot_performance(self):
        """method that plots stock object performance as percent """
        plt.plot(self.data['Close'].pct_change())
        plt.show()

def main():
    # uncomment (remove pass) code below to test
    test = Stock(symbol=[]) # optionally test custom data range
    print(test.data)
    test.plot_performance()
    test.plot_return_dist()


if __name__ == '__main__':
    main() 