from settings import IEX_KEY as cred
import requests
from Resources import *

class StockEquities:
    def __init__(self, symbol):
        self.symbol = symbol
        self.__public_key = cred.get_env_var("public_key")

    def advanced_fundamentals(self, period, **kwargs):
        """
        This function provides Reported Fundamental. It includes data as reported by the company from their financial
        statements - the income statement, balance sheet, and cash flow statement

        Credit Usage : 75,000 per record
        Data Timing : Real-time, Historical
        Data Schedule: Daily

        :param period: Either annual, quaterly, or ttm
        :param kwargs: Check https://iexcloud.io/docs/api/#stocks-equities
        :return:
        """
        endpoint = f'/time-series/fundamentals/{self.symbol}/{period}?'
        if 'range' in kwargs.keys():
            endpoint += f'range={kwargs["range"]}&'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Advanced Fundamentals'")
            # THROW EXCEPTION
       
        return json

    def advanced_stats(self):
        """
        Returns everything in key stats plus additional advanced stats such as EBITDA,
        ratios, key financial data, and more.

        Credit Usage: 3,000 per Symbol + Key Stats Weight
        Data Timing: End of Day
        Data Schedule: 4am, 5am ET

        :return: dict
        """
        endpoint = f'/stock/{self.symbol}/advanced-stats?'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def balance_sheet(self, **kwargs):
        """
        Pulls balance sheet data. Available quarterly or annually with the default being
        the last available quarter. This data is currently only available for U.S. symbols.

        Credit Usage: 3,000 per symbol per period
        Data Timing: End of Day
        Data Schedule: Updates at 8am, 9am UTC daily

        :param kwargs: Check https://iexcloud.io/docs/api/#stocks-equities
        :return:
        """
        endpoint = f'/stock/{self.symbol}/balance-sheet?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def book(self):
        """
        Returns the book.

        Credit Usage: 1 per quote returned
        Data Timing: Real-time + 15min delayed
        Data Schedule: Real-time

        :return:
        """
        endpoint = f'/stock/{self.symbol}/book?'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def cash_flow(self, **kwargs):
        """
        Pulls cash flow data. Available quarterly or annually, with the default being the
        last available quarter. This data is currently only available for U.S. symbols.

        Credit Usage: 1,000 per symbol per period
        Data Timing: End of Day
        Data Schedule: Updates at 8am, 9am UTC daily

        :param kwargs: Check https://iexcloud.io/docs/api/#stocks-equities
        :return:
        """
        endpoint = f"/stock/{self.symbol}/cash?"
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def chart(self):
        """
        Price charts can be built using the historical or intraday price endpoints
        :return:
        """
        pass

    def company(self):
        """
        Returns the basic information about symbol.

        Credit Usage: 1 per symbol
        Data Timing: End of Day
        Data Schedule: Update at 4am and 5am UTC everyday

        :return:
        """
        endpoint = f'/stock/{self.symbol}/company?'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def delayer_quote(self, **kwargs):
        """
        This returns the 15 minute delayed market quote.

        Credit Usage: 1 per symbol per quote
        Data Timing: 15min delayed
        Data Schedult: 4:30am - 8pm ET (Monday to Friday) when market is open

        :param kwargs: Check https://iexcloud.io/docs/api/#stocks-equities
        :return:
        """
        endpoint = f'/stock/{self.symbol}/delayed-quote?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def dividends(self, range=None):
        """
        Provides basic dividend data for US equities, ETFs, and Mutual Funds for the last 5 years.

        Credit Usage: 10 per symbol per period returned
        Data Timing: End of Day
        Data Schedule: Updated at 9am UTC everyday

        :param range: Check https://iexcloud.io/docs/api/#stocks-equities
        :return:
        """
        endpoint = f'/stock/{self.symbol}/divided'
        if range is not None:
            endpoint += f'/{range}?'
        else:
            endpoint += f'?'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def extended_hour_quote(self):
        pass

    def financials(self, **kwargs):
        """
        Pulls income statement, balance sheet, and cash flow data from the most recent reported quarter.

        Credit Usage: 5,000 per symbol per period
        Data Timing: End of Day
        Data Schedule: Update at 8am, 9am UTC daily

        :param kwargs: Check https://iexcloud.io/docs/api/#stocks-equities
        :return:
        """
        endpoint = f'/stock/{self.symbol}/financials?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def financial_as_reported(self, filling,  **kwargs):
        """
        As reported financials are pulled directly from the raw SEC filings.
        Returns raw financial data reported in 10-K and 10-Q filings.

        Credit Usage: 5,000 per filing per date returned
        Data Timing: Quarterly

        :param filling: 10-K (Annual report) or 10-Q (Quarterly report)
        :param kwargs: Check https://iexcloud.io/docs/api/#stocks-equities
        :return:
        """
        endpoint = f'/time-series/REPORTED_FINANCIALS/{self.symbol}/{filling}?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def fund_ownership(self):
        """
        Returns the top 10 fund holders, meaning any firm not defined as buy-side
        or sell-side such as mutual funds, pension funds, endowments, investment firms,
        and other large entities that manage funds on behalf of others.

        Credit Usage: 10,000 per symbol per period
        Data Timing: End of Day
        Data Schedule: Updates at 5am, 6am ET everyday

        :return:
        """
        endpoint = f'/stock/{self.symbol}/fund-ownership?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def historical_prices(self, range='1m', date=None, **kwargs):
        """
        Returns adjusted and unadjusted historical data for upto 15 years, and historical minute-by-minute
        intraday prices for the last 30 trailing calendar days. Usefull for building charts

        Credit Usage:
            Adjusted + Unadjusted:-
                10 per symbol per time interval returned.
            Adjusted close only:-
                2 per symbol per time interval returned.
        Data Timing: End of Day
        Data Schedule: Prior trading day adjusted data available after 4am ET (Tuesday to Saturday)

        :param range: Check https://iexcloud.io/docs/api/#stocks-equities
        :param date: Check https://iexcloud.io/docs/api/#stocks-equities
        :param kwargs: Check https://iexcloud.io/docs/api/#stocks-equities
        :return:
        """
        endpoint = f'/stock/{self.symbol}/chart'
        if date is not None:
            endpoint += f'/{range}/{date}?'
        else:
            endpoint += f'/{range}?'

        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def income_statement(self, **kwargs):
        """
        Pulls income statement data. Available quarterly or annually with the default being the last
        available quarter. This data is currently only available for U.S. symbols.

        Credit Usage: 1,000 per symbol per period
        Data Timing: End of Day
        Data Schedule: Updates at 8am, 9am UTC daily

        :param kwargs: Check https://iexcloud.io/docs/api/#stocks-equities
        :return:
        """
        endpoint = f'/stock/{self.symbol}/income?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def insider_roster(self):
        """
        Returns the top 10 insiders, with the most recent information.

        Credit Usage: 5,000 per symbol
        Data Timing: End of day
        Data Schedule: Updates at 5am, 6am ET everyday

        :return:
        """
        endpoint = f'/stock/{self.symbol}/insider-roster?'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def insider_summary(self):
        """
        Returns aggregated insiders summary data for the last 6 months.

        Credit Usage: 5,000 per symbol
        Data Timing: End of Day
        Data Schedule: Updates at 5am, 6am ET everyday

        :return:
        """
        endpoint = f'/stock/{self.symbol}/insider-summary?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def insider_transactions(self):
        """
        Returns insider transactions.

        Credit Usage: 50 per transaction
        Data Timing: End of Day
        Data Schedule: Updates at UTC everyday

        :return:
        """
        endpoint = f'/stock/{self.symbol}/insider-transactions?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def institutional_ownership(self):
        """
        Returns the top 10 institutional holders by default, defined as buy-side or sell-side firms.

        Credit Usage: 10,000 per symbol per period
        Data Timing: End of Day
        Data Schedule: Updates at 5am, 6am ET everyday

        :return:
        """
        endpoint = f'/stock/{self.symbol}/institutional_ownership?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def intraday_prices(self, **kwargs):
        """
        This function will return aggregated intraday prices in one-minute bucket for the current day.

        Credit Usage:
                1 per symbol per time interval upto a max use of 50 credits
            IEX Only intraday minute bar:-
                Free (Use the chartIEXOnly=True param)
        Data Timing:
            No delay for IEX data
            15min delay for market data
        Data Schedule:
            9:30 - 4pm ET (Monday to Friday) on regular market trading days
            9:30 - 1pm ET on early close trading days

        :param kwargs: Check https://iexcloud.io/docs/api/#stocks-equities
        :return:
        """
        endpoint = f'/stock/{self.symbol}/intraday-prices?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def key_stats(self):
        """
        Returns Key stats of the company and symbol.

        Credit Usage:
            5 per call per symbol for full stats
            1 per call per symbol for single stat filter
        Data Timing: End of Day
        Data Schedule: 8am, 9am ET

        :return:
        """
        endpoint = f'/stock/{self.symbol}/stats?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def largest_trade(self):
        """
        This returns 15 minute delayed, last sale eligible trades.

        Credit Usage: 1 per trade returned
        Data Timing: 15min delayed
        Data Schedule: 9:30 - 4pm ET (Monday to Friday)

        :return:
        """
        endpoint = f'/stock/{self.symbol}/largest-trades?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def logo(self):
        """
        This is a helper function, but the Google APIs url is standardized

        Credit Usage: 1 per logo
        Data Timing: End of Day
        Data Schedule: 8am UTC daily

        :return:
        """
        endpoint = f'/stock/{self.symbol}/logo?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def ohlc(self, market:bool):
        """
        Returns the official open and close for a give symbol. The official
        open is available as soon as 9:45am ET and the official close as soon
        as 4:15pm ET. Some stocks can report late open or close prices.

        Credit Usage: 2 per symbol
        Data Timing: 15min delayed
        Data Schedule: 9:30am - 5pm ET (Monday to Friday)

        :param market: Receives the ohlc for the market and not a particular stock.
        :return:
        """
        if market:
            endpoint = f'/stock/market/ohlc?'
        else:
            endpoint = f'/stock/{self.symbol}/ohlc?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def open_close_price(self):
        """
        Use ohlc

        :return:
        """
        pass

    def peer_group(self):
        """
        Returns a list of similar companies that are in the same sector.

        Credit Usage: 500 per call
        Data Timing: End of Day
        Data Schedule: 8am UTC daily

        :return:
        """
        endpoint = f'/stock/{self.symbol}/peers?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def previous_day_price(self, market:bool):
        """
        Returns previous day adjusted price data for one or more stocks

        Credit Usage: 2 per symbol
        Data Timing: End of Day
        Data Schedule: Available after 4am ET (Tuesday - Saturday)

        :param market: Receives the markets info and not a particular stock
        :return:
        """
        if market:
            endpoint = f'/stock/market/previous?'
        else:
            endpoint = f'/stock/{self.symbol}/previous?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def price_only(self):
        """
        Returns the price of the stock

        Credit Usage: 1 per call
        Data Timing: Real-time, 15min delayed, End of Day
        Data Schedule: 4:30am - 8pm ET (Monday to Friday)

        :return:
        """
        endpoint = f'/stock/{self.symbol}/price?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def quote(self):
        """
        Returns the latest quote.

        Credit Usage: 1 per quote called or streamed
        Data Timing: Real-time, 15min delayed, End of Day
        Data Schedule: 4:30am - 8pm ET (Monday to Friday)

        :return:
        """
        endpoint = f'/stock/{self.symbol}/quote?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def real_time_quote(self):
        """
        Use quote function.
        :return:
        """
        pass

    def sec_filings(self):
        """
        Use financial_as_reported function.
        :return:
        """
        pass

    def splits(self, range=None):
        """
        Returns the basic split data of a stock.

        Credit usage: 10 per symbol per record.
        Data Timing: End of Day
        Data Schedule: Updated at 9am UTC everyday

        :param range: Time range of information needed
        :return:
        """
        if range is not None:
            endpoint = f'/stock/{self.symbol}/splits/{range}?'
        else:
            endpoint = f'/stock/{self.symbol}/range?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def technical_indicators(self, indicator_name, **kwargs):
        """
        Returns the historical or intraday price for the given range, and the associated
        indicator for the price range.

        Credit Usage: 50 per indicator value + weight of the chart data returned (historical or intraday).
        Data Timing: On demand
        Data Schedule: On demand

        :param indicator_name: Indicator name
        :param kwargs: Check https://iexcloud.io/docs/api/#stocks-equities
        :return:
        """
        endpoint = f'/stock/{self.symbol}/indicator/{indicator_name}?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def volumen_by_venue(self):
        """
        This returns 15 minute delayed and 30 day average consolidated
        volume percentage of stock, by market.
        This call will always return 13 values, and will be sorted in
        ascending order by current day trading volume percentage

        Credit Usage: 20 per call
        Data Timing: 15min delayed
        Data Schedule: Updated during regular market hours 9:30am - 4pm ET

        :return:
        """
        endpoint = f'/stock/{self.symbol}/volume-by-venue?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response
