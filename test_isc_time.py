"""
Developer: Kelson Glaeske
Creation Date: 21/05/2026
version: 0
name: test_isc_time.py
Purpose: testing for isc_time.py
"""

from isc_time import get_deekday_for_date, ISCTime, timestamp_to_isc_date

# Test the deekday for May 30th 2026
# Note: In your tuple, months are 0-indexed (0=January, 1=February, etc.)
deekday = get_deekday_for_date(2026, 4, 30)  # May is index 4 (0=January)
print(f"The deekday for May 30th 2026 is: {deekday}")

# Test a few more dates
test_dates = [
    (2026, 0, 1),   # January 1st 2026 (should be Monday)
    (2026, 0, 10),  # January 10th 2026 (should be Starday)
    (2026, 0, 11),  # January 11th 2026 (should be Monday)
    (2026, 4, 30),  # May 30th 2026 (your specific test)
    (2026, 11, 30)  # December 30th 2026 (should be Starday)
]

for year, month, day in test_dates:
    deekday = get_deekday_for_date(year, month, day)
    month_name = ["January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"][month]
    print(f"{month_name} {day}, {year} is a {deekday}")
