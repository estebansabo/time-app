#See the time of any country in the world.

import pytz
from datetime import datetime

def get_time_in_country(country):
    try:
        country_timezone = pytz.country_timezones[country]
        tz = pytz.timezone(country_timezone[0])
        current_time = datetime.now(tz)
        return current_time.strftime("%H:%M:%S %Z")
    except KeyError:
        return "Invalid country code."

country = input("Enter a country code (e.g. 'us', 've', 'jp'): ")
print(get_time_in_country(country))
