import csv

__all__ = ["today", "getTodaysExercises"]

# returns which day of the program this is and what today's exercise focus is
def today ():

    # static for time being
    day = 1
    focus = ''

    with open('static/data/30day.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            
            # get focus for @code {day}
            if row[0] == str(day):
                focus = row[1]
    return day, focus


# reads todays exercise plan in from 30day.csv
def getTodaysExercises (day):
    todaysExercises = []

    with open('static/data/30day.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            
            # get exercises for given @code {day}
            if row[0] == str(day):
                for i in range(5):
                    todaysExercises.append(row[i+2])

    return todaysExercises