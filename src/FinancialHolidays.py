from datetime import date
from holidays import *

year = int(input("Enter year: "))
for date, name in sorted(financial_holidays(market = 'LSE', years = year).items()): # Replace LSE with your financial market code.
    print(date, name)
