# without the python datetime 
def wishes(new_year):
    if(new_year == 2021):
        print("Happy New Year, 2021")
wishes(2021)
print("From Inwerejosic with Love!")  

# datetime module imported

from datetime import datetime as dt


def greetings(verify):
    if verify.month == 1:
        return (f"Happy new year, welcome to {verify.year}")
    else:
        return(f"We still dey {verify.year}, wait small for the year")

date_check = dt.now()

print(greetings(date_check))

# kaggle example for testing


def greet(who='Colin'):
    print("Hello, ", who)
greet(who="Kaggle")   
greet("World")
