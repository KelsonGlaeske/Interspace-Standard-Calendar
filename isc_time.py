"""
Developer: Kelson Glaeske
Creation Date: 21/05/2026
version: 0
name: isc_time.py
Purpose: Establish functioning core code for the Interspace Standard Calendar, which is a new Calendar intended for use in space, including a new time constant that can solve the 2038 problem of Unix's time_t constant'
"""

import datetime

""" The ISC is a new Calendar meant to be a planet/stellar-system agnostic Calendar with metric like standards that is largely compatible with
living human time cycles. The time units of seconds, minutes, and hours are not affected as those are metric standards already. The day is defined as exactly 24 hours.

    This Calendar will be defined as retroactively created and started at January 1st, 2026 and the year of 2026 AD will carry over from the Gregorian Calendar
to the ISC from this moment onward.

    The ISC year is exactly 360 days long. There is 12 months of 30 days each with their names carried over from the Gregorian Calendar.
    Instead of weeks the ISC has what are labeled deeks, which are 10 days long. The first 7 days of the deek carry over from the Gregorian Calendar.
Three new days are appended from day 7 (Sunday) to the tenth day with the names in order: 'Lunaday', 'Solarday', and 'Starday'
As an additional note the months would all have exactly 3 deeks with symmetrical even division. The first of any month would always be a Monday and
the 30th of every month would always be a Starday. Additionally for optimal work-leisure ballance Deekdays (working days) would be defined as 6 days starting
on Monday and ending on Saturday while the dekend (the ISC equivalent of the weekend) would be 4 days long starting on Sunday and ending on Starday."""

# The ISC Epoch
isc_epoch = datetime.datetime(2026, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)

# Time Structure
class ISCTime:
    def __init__(self, seconds_since_epoch=0):
        self.seconds_since_epoch = seconds_since_epoch

    @classmethod
    def from_datetime(cls, dt):
        #Make ISCTime from datetime object
        seconds = int((dt - isc_epoch).total_seconds())
        return cls(seconds)

    @classmethod
    def now(cls):
        #get isc time
        now = datetime.datetime.now(datetime.timezone.utc)
        return cls.from_datetime(now)

    def to_datetime(self):
        #convert ISCTime back to datetime object
        return isc_epoch + datetime.timedelta(seconds=self.seconds_since_epoch)

    def __str__(self):
        return f"ISC Time: {self.seconds_since_epoch} seconds since epoch"

# Constant Calendar Values

iscYearDays = 360
iscYearMonths = 12
iscDeekLen = 10
iscM = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
iscDeek= ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Lunaday", "Solarday", "Starday")

# ISC Calendar Conversions
def timestamp_to_isc_date(timestamp):
    """Convert an ISC timestamp to ISC calendar components"""
    # Calculate total days and seconds since epoch
    total_days = timestamp // 86400  # 86400 seconds in a day
    remaining_seconds = timestamp % 86400

    # Calculate year, month, and day
    year = total_days // 360 + 2026  # 360 days per year, starting from 2026
    day_of_year = total_days % 360

    month = day_of_year // 30  # 30 days per month
    day = day_of_year % 30 + 1  # Days are 1-indexed

    # Calculate time components
    hour = remaining_seconds // 3600
    remaining_seconds %= 3600
    minute = remaining_seconds // 60
    second = remaining_seconds % 60

    # Calculate deek and day of deek
    deek = (day - 1) // 10 + 1  # Deeks are 1-indexed
    day_of_deek = (day - 1) % 10  # 0-indexed for tuple access

    return {
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'minute': minute,
        'second': second,
        'deek': deek,
        'day_of_deek': day_of_deek,
        'day_name': iscDeek[day_of_deek],
        'month_name': iscM[month]
    }

def format_isc_date(date_dict):
    """Format an ISC date dictionary into a readable string"""
    return f"{date_dict['day_name']}, {date_dict['day']} {date_dict['month_name']} {date_dict['year']} (Deek {date_dict['deek']}, Day {date_dict['day_of_deek']+1}) {date_dict['hour']:02d}:{date_dict['minute']:02d}:{date_dict['second']:02d}"

# Deekday Display functions

def get_current_deekday():
    """Get the name of the current deekday"""
    current_time = ISCTime.now()
    return get_deekday(current_time.seconds_since_epoch)

def get_deekday_for_date(year, month, day):
    """Get the name of the deekday for a specific ISC date
    Args:
        year: ISC year (e.g., 2026)
        month: Month index (0-11, where 0=January)
        day: Day of month (1-30)
    Returns:
        Name of the deekday (e.g., "Tuesday")
    """
    # Calculate total days since epoch
    days_from_start = (year - 2026) * 360 + month * 30 + (day - 1)
    day_of_deek = days_from_start % 10
    return iscDeek[day_of_deek]

def get_deekday_by_timestamp(timestamp):
    """Get the name of the deekday for a given ISC timestamp"""
    return get_deekday(timestamp)

def get_deekday(timestamp):
    """Get the name of the deekday for a given timestamp"""
    # Convert timestamp to ISC date
    isc_date = timestamp_to_isc_date(timestamp)
    # Return the day name from the tuple
    return isc_date['day_name']

def get_deekday_number(timestamp):
    """Get the number of the deekday (0-9) for a given timestamp"""
    # Convert timestamp to ISC date
    isc_date = timestamp_to_isc_date(timestamp)
    # Return the day number (0-9)
    return isc_date['day_of_deek']
