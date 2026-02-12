from datetime import date
from dateutil.relativedelta import relativedelta

start_date = date(2015, 6, 10)
last_completed_date = date(2026, 12, 15)
today = date(2027, 1, 8) #date.today

anchor_day = start_date.day

end_date = last_completed_date + relativedelta(
    months=1,
    day=anchor_day
)

if start_date <= today < end_date:
    print("Within rolling window")
else:
    print("Not")
