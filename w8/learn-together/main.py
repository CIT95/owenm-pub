import datetime
import art


# Adapted this function from https://stackoverflow.com/a/15226988
def format_date(entry):
    """Takes an American date format (mm/dd/yyyy) input and converts it into
    the date datatype"""
    m, d, y = map(int, entry.split("/"))
    return datetime.date(y, m, d)


def format_time(entry):
    """Takes a time as a string (hh:mm) and formats it as
    the time datatype"""
    h, m = map(int, entry.split(":"))
    return datetime.time(h, m)


print(art.logo)

sleep_log = {}  # Set up the log dictionary

cont = True
while cont:  # Some flow control
    # Get inputs for the date, beginning, and end of a sleep.
    sleep_date = format_date(input("\nEnter the date of the night you fell"
                                   " asleep on, formatted as mm/dd/yyyy: "))
    start_time = format_time(input("Enter the time you fell asleep,"
                                   " formatted as hh:mm: "))
    end_time = format_time(input("Enter the time that you woke up the next"
                                 " day, formatted as hh:mm: "))

    # Add the above data to the log
    sleep_log[sleep_date] = [start_time, end_time]

    # Ask user to continue
    if input("\nWould you like to add another entry? (y/n) ") == "y":
        cont = True
    else:
        cont = False

# Find the longest sleep
greatest_value = datetime.timedelta(days=0)
for day in sleep_log:
    start = datetime.datetime.combine(day, sleep_log[day][0]) + \
            datetime.timedelta(hours=12)
    end = datetime.datetime.combine(day, sleep_log[day][1]) + \
        datetime.timedelta(days=1)

    duration = end - start
    if duration >= greatest_value:
        greatest_value = duration
        longest_sleep = [day, duration]

# Find the shortest sleep
least_value = datetime.timedelta(days=999)
for day in sleep_log:
    start = datetime.datetime.combine(day, sleep_log[day][0]) + \
            datetime.timedelta(hours=12)
    end = datetime.datetime.combine(day, sleep_log[day][1]) + \
        datetime.timedelta(days=1)

    duration = end - start
    if duration <= greatest_value:
        greatest_value = duration
        shortest_sleep = [day, duration]

# Find the average sleep length
sleep_lengths = []
for day in sleep_log:
    start = datetime.datetime.combine(day, sleep_log[day][0]) + \
            datetime.timedelta(hours=12)
    end = datetime.datetime.combine(day, sleep_log[day][1]) + \
        datetime.timedelta(days=1)

    duration = end - start
    sleep_lengths.append(duration.seconds)
average_sleep = sum(sleep_lengths) // len(sleep_lengths)

# Print stats
print(f"\nYour longest sleep was on {longest_sleep[0].strftime('%m/%d/%Y')}"
      f" and lasted {longest_sleep[1].seconds // 3600}"
      f" hours and {(longest_sleep[1].seconds // 60) % 60} minutes")

print(f"Your shortest sleep was on {shortest_sleep[0].strftime('%m/%d/%Y')}"
      f" and lasted {shortest_sleep[1].seconds // 3600}"
      f" hours and {(shortest_sleep[1].seconds // 60) % 60} minutes")

print(f"Your average sleep length was {average_sleep // 3600}"
      f" hours and {(average_sleep // 60) % 60} minutes")
