from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

# utc_now = datetime.now(timezone.utc)
# print(utc_now)

# local_now = utc_now.astimezone()
# print(local_now)

# new_york_tz = zoneinfo.ZoneInfo('Asia/Kolkata')
# ny_now = utc_now.astimezone(tz=new_york_tz)
# print(ny_now)

# france_tz = zoneinfo.ZoneInfo('Europe/Paris')
# france_now = utc_now.astimezone(tz = france_tz)
# print(france_now)

#Timezone keys for creating the zoneinfo objects
local_now = datetime.now()
# local_now = local_now.replace(microsecond=0)
zones = (
    'Europe/Paris',
    'Europe/London',
    'Asia/Hong_Kong',
    'Africa/Nairobi'
)
#Get the current time in UTC
# utc_now = datetime.now(tz=timezone.utc)
for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    # required_time = utc_now.astimezone(tz)
    required_time = local_now.astimezone(tz)
    city = zone.split('/')[-1]
    print(f'The time in {city} is {required_time.strftime("%m/%d/%Y %H:%M:%S")}')