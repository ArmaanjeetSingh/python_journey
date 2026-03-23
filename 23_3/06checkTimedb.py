import sqlite3
from datetime import datetime
from zoneinfo import  ZoneInfo

db = sqlite3.connect("account.db",detect_types = sqlite3.PARSE_DECLTYPES)
for row in db.execute("SELECT time FROM history"):
    utc_time = row[0]
    if isinstance(utc_time, str):
        utc_time = datetime.fromisoformat(utc_time)

    local_time = utc_time.astimezone(ZoneInfo('Asia/Kolkata'))
    print('{}\t{}'.format(utc_time,local_time))

db.close()