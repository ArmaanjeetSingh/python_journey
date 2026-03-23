import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo
import pickle

db = sqlite3.connect("account2.db",detect_types = sqlite3.PARSE_DECLTYPES)

for row in db.execute('SELECT * FROM history'):
    utc_time = row[0]
    pickled_zone = row[3]
    zone = pickle.loads(pickled_zone)
    local_time = utc_time.astimezone(zone)
    print(local_time,zone,sep='\t')