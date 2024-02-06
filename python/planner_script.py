# Example script that generates planner booklets for January 2024

import planner as pln
import page as pg
import holiday
import quote
import calendar as cal
import datetime

# Create an empty planner
start_date = datetime.date.fromisoformat('2024-01-01')
end_date = datetime.date.fromisoformat('2024-02-01') #not including
jan24_pln = pln.Planner(start_date, end_date)

# Daily prompt questions
promptList = [
    "How is your mood?",
    "What are you grateful for?",
    "Who did you help?",
]

# Add pages to planner
page_cnt = 0
jan24_pln.addPage(pg.Cover("", 'January', '2024', f'&#8220{quote.quotes["Mary Shelley"][3]}&#8221</br>Mary Shelley'))
jan24_pln.addPage(pg.HabitLeft("", "Goals & Intentions"))
jan24_pln.addPage(pg.HabitRight("", "Self Encouragement"))
jan24_pln.addPage(pg.CalLeft("", 1, 2024, holiday.holidayMaster))
jan24_pln.addPage(pg.CalRight("", 1, 2024, holiday.holidayMaster))
date_pointer = start_date
week = datetime.timedelta(days=7)
while date_pointer < end_date:
    jan24_pln.addPage(pg.Week("", date_pointer))
    jan24_pln.addWeekofDays(date_pointer, promptList)
    date_pointer += week
    page_cnt += 8
page_cnt += 8
for i in range(4-page_cnt%4):
    jan24_pln.addPage(pg.Lined(""))
for i in range(2):
    jan24_pln.addPage(pg.Graph(""))
jan24_pln.addPage(pg.Question("", "What did you learn this month?"))

# Create planners
jan24_pln.createPlanner(filename='out_5x8.html', size='5x8')
jan24_pln.createPlanner(filename='out_A5slim.html', size='A5slim')
jan24_pln.createPlanner(filename='out_3x5.html', size='3x5')
jan24_pln.createPlanner(spread='reader', filename='out_reader.html', size='A5slim')
