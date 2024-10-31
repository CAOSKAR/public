import datetime
from datetime import timezone
import pytz
now = datetime.datetime.now()
nowform = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")##timezone.utc
nowformutc = datetime.datetime.now(timezone.utc).strftime("%d.%m.%Y %H:%M:%S")##timezone.utc
nowformutc1 = datetime.datetime.now(pytz.timezone('Europe/Berlin')).strftime("%d.%m.%Y %H:%M:%S")##timezone.utc
nowformutc2 = datetime.datetime.now(pytz.timezone('Europe/Sofia')).strftime("%d.%m.%Y %H:%M:%S")##timezone.utc
print(now.date())
print(nowform)
print("Datetime in UTC: ",nowformutc)
print("Datetime in Berlin: ",nowformutc1)
print("Datetime in Sofia: ",nowformutc2)
print(now.year)
print(now.month)
print(now.day)
print(now.strftime('%d.%m.%Y'))