import datetime as dt
print(f"Yesterday: {dt.date.today() - dt.timedelta(1)}\nToday: {dt.date.today()}\nTomorrow: {dt.date.today() + dt.timedelta(1)}")