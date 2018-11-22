import datetime
import pytz

dt_mtn = datetime.datetime.now(tz=pytz.timezone('Asia/Singapore'))
print(dt_mtn.strftime('%d %B, %Y %H %M'))