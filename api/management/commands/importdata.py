import csv
import yaml
from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import Restaurant, Restaurant_names
from datetime import datetime


class Command(BaseCommand):
    help = 'Imports csv data to database'

    def handle(self, *args, **kwargs):
        time_format_with_minutes = '%I:%M %p'
        time_format = '%I %p'

        with open('finalhours.csv') as csv_file:
            restaurant_names = csv.reader(csv_file, delimiter=',')

            for index, data in enumerate(restaurant_names):
                restaurant_name = data[0].strip()
                restaurant_details = yaml.load(data[2])
                restaurant_obj, created = Restaurant_names.objects.get_or_create(name=restaurant_name)
                open_dict = {}
                close_dict = {}
                for day in restaurant_details:
                    opening_time = restaurant_details[day][0]
                    closing_time = restaurant_details[day][1]
                    try:
                        opening_time = datetime.strptime(opening_time, time_format).time()
                    except ValueError:
                        opening_time = datetime.strptime(opening_time, time_format_with_minutes).time()
                    try:
                        closing_time = datetime.strptime(closing_time, time_format).time()
                    except ValueError:
                        closing_time = datetime.strptime(closing_time, time_format_with_minutes).time()
                    open_dict[str(day)] = str(opening_time)
                    close_dict[str(day)] = str(closing_time)
                details_obj, created = Restaurant.objects.get_or_create(
                        restaurant = restaurant_obj,
                        opening_time = open_dict,
                        closing_time = close_dict
                        )
                self.stdout.write(self.style.SUCCESS('Success: ' + str(index + 1) + ' rows completed.'))
