import os
import requests

from Resources import *
from dotenv import load_dotenv

class InterfaceError(Exception):
    def __init__(self):
        super()


class GetClass:
    def __init__(self, symbol):
        load_dotenv()
        self.symbol = symbol
        self.TDA_API_KEY = os.getenv("TDA_KEY")
        self.IEX_API_KEY = os.getenv("IEX_KEY")

    def analyst_recommendations(self):
        """
        Gives the analayst recommendations and price targets for equities.
        Data Weighting
        10,000 per record

        Data Timing
        End of day

        Data Schedule
        Updates Tuesday - Saturday at 11am UTC

        Data Source(s)
        Invisage
        :return:
        """
        endpoint = f'/time-series/CORE_ESTIMATES/{self.symbol}/?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        print(url)

        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'CORE_ESTIMATES'")
            raise InterfaceError("API returned null response.")

        return json



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
        endpoint = f'/stock/{self.symbol}/balance-sheet/?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        print(url)
        
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Balance Sheet'")
            raise InterfaceError("API returned null response.")

        return json



    def bonus_issue(self, period,last):
        """
        Obtain up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.
        IEX URL: https://iexcloud.io/docs/api/#bonus-issue
        """
        print(self.symbol)
        # last must be an integer. Not sure how large last can be or what the set "period" is by default
        # cannot use period here such as quarterly or annual
        endpoint = f'/time-series/advanced_bonus/{self.symbol}?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Bonus Issue'")
            raise InterfaceError("API returned null response.")

        return json



    def book(self):
        """
        Returns the book.
        Credit Usage: 1 per quote returned
        Data Timing: Real-time + 15min delayed
        Data Schedule: Real-time
        :return:
        """
        print(self.symbol)
        endpoint = f'/stock/{self.symbol}/book/?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Book'")
            raise InterfaceError("API returned null response.")

        return json



    def cash_flow(self, period,last):
        """
        Pulls cash flow data. Available quarterly or annually, with the default being the
        last available quarter. This data is currently only available for U.S. symbols.
        Credit Usage: 1,000 per symbol per period
        Data Timing: End of Day
        Data Schedule: Updates at 8am, 9am UTC daily
        :param kwargs: Check https://iexcloud.io/docs/api/#stocks-equities

        examples...
        /stock/aapl/cash-flow
        /stock/aapl/cash-flow?period=annual
        period can be 'annual' or 'quarter'
        last is a number that can be up to 12 with quarter. For annual it can go up to 4 years.
        (i.e  /stock/aapl/cash-flow?period=annual
        :return:
        """
        endpoint = f"/stock/{self.symbol}/cash-flow/{period}?"
        # the value of period can be period='annual' or period='quarter'
        # the value of last needs to be up to 12 if period = quarter and up to 4 if period = annual
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Cash Flow'")
            raise InterfaceError("API returned null response.")

        return json



    def ceo_compensation (self):
        """
        This endpoint provides CEO compensation for a company by symbol.
        IEX URL: https://iexcloud.io/docs/api/#ceo-compensation
        :return:
        """
        endpoint = f"/stock/{self.symbol}/ceo-compensation/?"
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'CEO Compensation'")
            raise InterfaceError("API returned null response.")

        return json



    def charts(self):
        return


    # def collections(self,sector):
    #     """
    #     Returns an array of quote objects for a given collection type. Currently supported collection types are sector, tag, and list
    #     Examples
    #     /stock/market/collection/sector?collectionName=Technology
    #     /stock/market/collection/tag?collectionName=Airlines
    #     /stock/market/collection/list?collectionName=mostactive
    #     :return:
    #     """
    #     print(sector)
    #     endpoint = f"/stock/market/collection/tag?collectionName=Airlines/?"
    #     url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
    #     print(url)
    #     
    #     print(response.raw)
    #     print(response.headers)
    #     print(response.content)
    #     print(response.json())
    #     return response

    def company(self):
        """
        Returns the basic information about symbol.
        Credit Usage: 1 per symbol
        Data Timing: End of Day
        Data Schedule: Update at 4am and 5am UTC everyday
        :return:
        """
        endpoint = f'/stock/{self.symbol}/company?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Company'")
            raise InterfaceError("API returned null response.")

        return json



    def delayed_quote(self, **kwargs):
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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Delayed Quote'")
            raise InterfaceError("API returned null response.")

        return json



    def distribution(self):
        return

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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Dividends'")
            raise InterfaceError("API returned null response.")

        return json



    def earnings_today(self):
        return

    def extended_hour_quote(self):
        pass

    def financials_as_reported(self):
        return

    def financials(self):
        return

    def fundamentals(self, period, **kwargs):
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
            url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Fundamentals'")
            raise InterfaceError("API returned null response.")

        return json



    def fundamental_valuations(self):
        return

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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Historical Prices'")
            raise InterfaceError("API returned null response.")

        return json



    def income_statement(self):
        return

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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Income Statement'")
            raise InterfaceError("API returned null response.")

        return json



    def insider_roster(self):
        return

    def financial_as_reported(self, filling, **kwargs):
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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Reported Financials'")
            raise InterfaceError("API returned null response.")

        return json



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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Financials'")
            raise InterfaceError("API returned null response.")

        return json



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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Fund Ownership'")
            raise InterfaceError("API returned null response.")

        return json



    def fundamentals(self):
        return

    def fundamental_valuations(self):
        return

    def historical_prices(self):
        return


    def insider_roster(self):
        """
        Returns the top 10 insiders, with the most recent information.
        Credit Usage: 5,000 per symbol
        Data Timing: End of day
        Data Schedule: Updates at 5am, 6am ET everyday
        :return:
        """
        endpoint = f'/stock/{self.symbol}/insider-roster?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Insider Roster'")
            raise InterfaceError("API returned null response.")

        return json



    def insider_summary(self):
        """
        Returns aggregated insiders summary data for the last 6 months.
        Credit Usage: 5,000 per symbol
        Data Timing: End of Day
        Data Schedule: Updates at 5am, 6am ET everyday
        :return:
        """
        endpoint = f'/stock/{self.symbol}/insider-summary?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Insider Summary")
            raise InterfaceError("API returned null response.")

        return json



    def insider_transactions(self):
        """
        Returns insider transactions.
        Credit Usage: 50 per transaction
        Data Timing: End of Day
        Data Schedule: Updates at UTC everyday
        :return:
        """
        endpoint = f'/stock/{self.symbol}/insider-transactions?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Insider Transations'")
            raise InterfaceError("API returned null response.")

        return json



    def institutional_ownership(self):
        """
        Returns the top 10 institutional holders by default, defined as buy-side or sell-side firms.
        Credit Usage: 10,000 per symbol per period
        Data Timing: End of Day
        Data Schedule: Updates at 5am, 6am ET everyday
        :return:
        """
        endpoint = f'/stock/{self.symbol}/institutional_ownership?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Institutional Ownership'")
            raise InterfaceError("API returned null response.")

        return json



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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Intraday Prices")
            raise InterfaceError("API returned null response.")

        return json



    def ipo_calendar(self):
        return

    def largest_trade(self):
        """
        This returns 15 minute delayed, last sale eligible trades.
        Credit Usage: 1 per trade returned
        Data Timing: 15min delayed
        Data Schedule: 9:30 - 4pm ET (Monday to Friday)
        :return:
        """
        endpoint = f'/stock/{self.symbol}/largest-trades?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        print(url)
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Largest Trades'")
            raise InterfaceError("API returned null response.")

        return json



    def largest_trades(self):
        return

    def list(self):
        return

    def logo(self):
        """
        This is a helper function, but the Google APIs url is standardized
        Credit Usage: 1 per logo
        Data Timing: End of Day
        Data Schedule: 8am UTC daily
        :return:
        """
        endpoint = f'/stock/{self.symbol}/logo?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Logo'")
            raise InterfaceError("API returned null response.")

        return json



    def market_volume(self):
        return

    def market(self):
        return

    def ohlc(self, market: bool):
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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'OHLC'")
            raise InterfaceError("API returned null response.")

        return json



    def open_close_price(self):
        return

    def peer_groups(self):
        return

    def previous_day_price(self):
        return

    def price_only(self):
        return

    def quote(self):
        return


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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Key Stats'")
            raise InterfaceError("API returned null response.")

        return json




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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Peers'")
            raise InterfaceError("API returned null response.")

        return json



    def previous_day_price(self, market: bool):
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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Previous'")
            raise InterfaceError("API returned null response.")

        return json



    def price_only(self):
        """
        Returns the price of the stock
        Credit Usage: 1 per call
        Data Timing: Real-time, 15min delayed, End of Day
        Data Schedule: 4:30am - 8pm ET (Monday to Friday)
        :return:
        """
        endpoint = f'/stock/{self.symbol}/price?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        print(url)
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Price'")
            raise InterfaceError("API returned null response.")

        return json




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

    def return_of_capital(self):
        return

    def right_to_purchase(self):
        return

    def rights_issue(self):
        return

    def sector_performance(self):
        return

    def sector_performance(self):
        return

    def sec_filings(self):
        return

    def security_reclassificaiton(self):
        return

    def security_swap(self):
        return

    def spinoff(self):
        return

    def splits(self):
        return

    def stats(self):
        """
        Returns everything in key stats plus additional advanced stats such as EBITDA,
        ratios, key financial data, and more.
        Credit Usage: 3,000 per Symbol + Key Stats Weight
        Data Timing: End of Day
        Data Schedule: 4am, 5am ET
        :return: dict
        """
        endpoint = f'/stock/{self.symbol}/advanced-stats?'
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Advanced Stats'")
            raise InterfaceError("API returned null response.")

        return json



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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Indicator'")
            raise InterfaceError("API returned null response.")

        return json




    def upcoming_events(self):
        return

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
        url = IEX_BASE_URL + endpoint + f'token={self.IEX_API_KEY}'
        try:
            response = requests.get(url)
            json = response.json()
        except:
            print("Request error for symbol " + self.symbol + " on IEX Request 'Splits'")
            raise InterfaceError("API returned null response.")

        return json




    def volume_by_venue(self):
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
        return

    def tda_getprice(self,periodtype,period,frequencytype,frequency):
        """
        examples from TDA API https://developer.tdameritrade.com/content/price-history-samples
        :param periodtype: this defines a period of time such as day, month, year
        :param period: how many periods do you want to look at? If you said your periodtype was day, then a period of 5 will be 5 days. If period type was year and the period is set to 3 you will get 3 years of data
        :param frequencytype: Within each period how many times do you wanta data to be given? Within 5 days, you can get data for every minute within that week... frequencytype=minute
        :param frequency: Whatever your frequencytype is... minute, daily, month, year -- you can change the frequency=1, frequency=5, frequency=15(minutes,days,months,years)
        :return:
        """
        url = f"https://api.tdameritrade.com/v1/marketdata/{self.symbol}/pricehistory?apikey={self.TDA_API_KEY}&periodType={periodtype}&period={period}&frequencyType={frequencytype}&frequency={frequency}"
        print(url)
        response = requests.get(url).json()
        print(response)
        return response
