import csv
import yaml
from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import Restaurant, Restaurant_data
from datetime import datetime


class Command(BaseCommand):
    help = 'Imports csv data to database'

    def handle(self, *args, **kwargs):
        time_format_with_minutes = '%I:%M %p'
        time_format = '%I %p'

        with open('finalhours.csv') as csv_file:
            restaurant_data = csv.reader(csv_file, delimiter=',')

            for index, data in enumerate(restaurant_data):
                restaurant_name = data[0].strip()
                restaurant_details = yaml.load(data[2])
                restaurant_obj, created = Restaurant_data.objects.get_or_create(name=restaurant_name)
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

                    details_obj, created = Restaurant.objects.get_or_create(
                        restaurant = restaurant_obj,
                        opening_time = opening_time,
                        closing_time = closing_time,
                        day=str(day)
                        )
                self.stdout.write(self.style.SUCCESS('Success: ' + str(index + 1) + ' rows completed.'))
