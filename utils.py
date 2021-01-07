from random import randrange
from datetime import timedelta
from datetime import datetime
import random


def wrap_html(input):
    base = "<html><body>{}</body></html>"
    return base.format(input)


def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def get_fake_date_time():
    date_time_str = "1/1/20 12:00:00"
    start = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
    date_time_str = "1/12/20 12:00:00"
    end = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
    random_date_value = random_date(start, end)
    return random_date_value, random_date_value + timedelta(hours=random.choice([.5, 1]))
