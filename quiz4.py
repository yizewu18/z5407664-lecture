""" yf_example2.py

Example of a function to download stock prices from Yahoo Finance.
"""

import yfinance as yf


def yf_prc_to_csv(tic, pth, start=None, end=None):
    """ Downloads analysts recommendation from Yahoo Finance and saves the
    information in a CSV file

    Parameters
    ----------
    tic : str
        Ticker

    pth : str
        Location of the output CSV file

    start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)

# Example
if __name__ == "__main__":
    tic = 'QAN.AX'
    pth = 'qan_stk_prc.csv'
    yf_prc_to_csv(tic, pth)

    tic = "QAN.AX"
    start = '{year}-01-01'
    end = f'{year}-12-31'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    df = yf_example2.yf_prc_to_csv(
        tic=tic,
        pth=pth,
        start=start,
        end=end)

    if __name__ == "__main__":
        year = 2020
        qan_prc_to_csv(year)
