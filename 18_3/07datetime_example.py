import datetime as dt
import datetime
# from datetime import datetime never call objects inside a module as same name as the module itself

today = dt.datetime.today()
now = dt.datetime.now()
utc_now =  datetime.datetime.now(datetime.UTC)

print(today)
print(now)
print(utc_now)
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# Define UK timezone
uk_tz = ZoneInfo("Europe/London")

# Example input
year, month, day = 2026, 3, 18
hour, minute = 10, 30

# Time difference to add (e.g., 2 hours 45 minutes)
td = timedelta(hours=2, minutes=45)

# Step 1: Create UK time
uk_time = datetime(year, month, day, hour, minute, tzinfo=uk_tz)
print("Original UK Time:", uk_time)

# Step 2: Convert to UTC
utc_time = uk_time.astimezone(timezone.utc)
print("Converted to UTC:", utc_time)

# Step 3: Add time delta in UTC
utc_time += td
print("UTC after adding timedelta:", utc_time)

# Step 4: Convert back to UK time
uk_time = utc_time.astimezone(uk_tz)
print("Final UK Time:", uk_time)