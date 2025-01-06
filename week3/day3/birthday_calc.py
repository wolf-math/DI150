from datetime import datetime, timedelta

def birthday_countdown(birthday_str):
    today = datetime.now()
    this_year_birthday = datetime.strptime(f"{today.year}-{birthday_str}", "%Y-%m-%d")
    
    # If birthday has already passed this year, calculate for next year
    if this_year_birthday < today:
        this_year_birthday = this_year_birthday.replace(year=today.year + 1)
    
    # Calculate the difference between now and the next birthday
    countdown = this_year_birthday - today
    
    # Extract days, hours, minutes, and seconds
    days = countdown.days
    hours, remainder = divmod(countdown.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f"My birthday is in {days} days, and {hours:02}:{minutes:02}:{seconds:02}!"

my_birthday = "12-25" 
print(birthday_countdown(my_birthday))
