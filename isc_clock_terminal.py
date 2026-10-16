"""
Developer: Kelson Glaeske
Creation Date: 21/05/2026
version: 0
name: isc_clock_terminal.py
Purpose: Make a clock that tells isc date and time in real-time in the terminal.
"""

import sys
import time
import datetime

# Import your existing code
from isc_time import ISCTime, timestamp_to_isc_date, format_isc_date, isc_epoch

def clear_screen():
    """Clear the terminal screen"""
    print("\033[2J\033[H", end="")

def isc_clock():
    """Display an ISC clock that updates every second"""
    print("Interspace Standard Calendar Clock (Press Ctrl+C to exit)")
    print("=" * 50)

    try:
        while True:
            # Get current ISC time
            current_isc_time = ISCTime.now()
            current_isc_date = timestamp_to_isc_date(current_isc_time.seconds_since_epoch)

            # Clear screen and display clock
            clear_screen()
            print("=" * 50)
            print("        INTERSPACE STANDARD CALENDAR CLOCK")
            print("=" * 50)
            print()
            print(f"  {format_isc_date(current_isc_date)}")
            print()
            print("-" * 50)
            print(f"  Unix Timestamp: {int((datetime.datetime.now(datetime.timezone.utc) - datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)).total_seconds())}")
            print(f"  ISC Timestamp:  {current_isc_time.seconds_since_epoch}")
            print("-" * 50)
            print(f"  Day of Deek:    {current_isc_date['day_of_deek']+1}/10 ({current_isc_date['day_name']})")
            print(f"  Deek:           {current_isc_date['deek']}/3 in {current_isc_date['month_name']} {current_isc_date['year']}")
            print(f"  Work/Life:      {'Dekend' if current_isc_date['day_of_deek'] >= 6 else 'Deekday'}")
            print()
            print("=" * 50)
            print("Press Ctrl+C to exit")

            # Wait 1 second
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nClock stopped. Goodbye!")

if __name__ == "__main__":
    isc_clock()
