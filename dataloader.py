import re
import csv
from datetime import datetime

regex_pattern = '(.[^\d]*)(\s*(\d{1,2}(:\d{2})?\s*(am|pm))\s*-\s*(\d{1,2}(:\d{2})?\s*(am|pm)))'

day_mapping = {
    'Mon': 0,
    'Tue': 1,
    'Tues': 1,
    'Wed': 2,
    'Weds': 2,
    'Thu': 3,
    'Thurs': 3,
    'Fri': 4,
    'Sat': 5,
    'Sun': 6
}

with open('finalhours.csv', 'w') as finalfile:
    writer = csv.writer(finalfile)
    with open('hours.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            finaldays = {}
            timelist = row[1].split('/')
            for item in timelist:
                m = re.match(regex_pattern, item)
                days = m.group(1).strip().split(',')
                start_time = m.group(3).strip()
                end_time = m.group(6).strip()
                
                for day in days:
                    day = day.strip()
                    if '-' not in day:
                        finaldays[day_mapping[day]] = [start_time, end_time]
                    elif '-' in day:
                        day = day.split('-')
                        day[0] = day[0].strip()
                        day[1] = day[1].strip()
                        if day_mapping[day[1]] < day_mapping[day[0]]:
                            for i in range(day_mapping[day[0]], day_mapping[day[0]]+day_mapping[day[1]]+2):
                                finaldays[i%7] = [start_time, end_time]    
                        else:
                            for i in range(day_mapping[day[0]], day_mapping[day[1]]+1):
                                finaldays[i] = [start_time, end_time]
            writer.writerow([row[0],row[1],finaldays])
