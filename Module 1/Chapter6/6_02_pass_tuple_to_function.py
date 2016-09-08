import datetime
def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) /2), date)

mid_value, date = middle(("GOOG", 613.30, 625.86, 610.50), 
        datetime.date(2010, 1, 6))
