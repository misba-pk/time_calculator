def add_time(start, duration, starting_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(":"))
    duration_hours, duration_minutes = map(int, duration.split(":"))
    
    total_minutes = start_hours * 60 + start_minutes + duration_hours * 60 + duration_minutes
    days_later = total_minutes/(24 * 60)
    if days_later>1:
       days_later = round(days_later)
    remaining_minutes = total_minutes % (24 * 60)
    
    new_hours = remaining_minutes // 60
    new_minutes = remaining_minutes % 60
    new_period = period
    
    if new_hours >= 12:
        new_period = "PM" if period == "AM" else "AM"
    
    if new_hours == 0:
        new_hours = 12
    elif new_hours > 12:
        new_hours -= 12
    
    result = f"{new_hours}:{new_minutes:02d} {new_period}"
    
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (starting_day_index + int(days_later)) % 7
        new_day = days_of_week[new_day_index]
        result += f", {new_day}"
    
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"
    
    return result


print(add_time("11:06 PM", "2:02"))
