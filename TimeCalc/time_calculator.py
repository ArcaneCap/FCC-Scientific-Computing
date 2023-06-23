def add_time(t1, t2, day=False):
    # List of days of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  
    # Splitting the first time input into hour, minute, and meridiem (AM/PM)
    t1 = t1.split()
    t1_hour, t1_minute = t1[0].split(':')
    t1_meridem = t1[1].upper()

    # Splitting the second time input into hour and minute
    t2 = t2.split()
    t2_hour, t2_minute = t2[0].split(':')

    # Converting t1_hour to 24-hour format if it is in the PM
    if t1_meridem == 'PM':
        t1_hour = int(t1_hour) + 12

    # Calculating the combined minute and surplus 
    combined_minute = int(t1_minute) + int(t2_minute)
    if combined_minute > 60:
        new_minute = combined_minute % 60
        add_hour = 1
    else:
        new_minute = combined_minute
        add_hour = 0

    # Calculating the combined hour, including the additional hour if there surplus in minutes
    combined_hour = int(t1_hour) + int(t2_hour) + add_hour

    # Calculating the number of days to add based on the combined hour
    days_to_add = combined_hour // 24

    # Formatting the hour and meridiem for display
    if combined_hour >= 12:
        new_hour = combined_hour % 24
        if new_hour >= 12:
            if new_hour > 12:
                formatted_hour = new_hour - 12
            else:
                formatted_hour = new_hour
            formatted_meridem = 'PM'
        elif new_hour == 0:
            formatted_hour = 12
            formatted_meridem = 'AM'
        else:
            formatted_hour = new_hour
            formatted_meridem = 'AM'
    else:
        formatted_hour = combined_hour
        formatted_meridem = t1_meridem

    # Formatting the new day if a starting day was provided
    if day != False:
        t1_Day = day.capitalize()
        day_index = days.index(t1_Day)
        new_day = days[(day_index + days_to_add) % 7]
        formattedDay = f', {new_day}'
    else:
        formattedDay = ''

    # Formatting the difference information based on the number of days to add
    if days_to_add == 1:
        formatted_difference = ' (next day)'
    elif days_to_add > 1:
        formatted_difference = f' ({days_to_add} days later)'
    else:
        formatted_difference = ''

    # Constructing the final formatted time string
    new_time = "{}:{:02d} {}{}{}".format(formatted_hour, new_minute, formatted_meridem, formattedDay, formatted_difference)

    return new_time
