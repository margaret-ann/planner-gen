#!/usr/bin/env python
# coding: utf-8

import planner as pln
import page as pg
import holiday
import quote
import calendar as cal

# writing the html
feb24 = [
    pg.Cover("", 'February', '2024', f'&#8220{quote.quotes["Joan of Arc"][0]}&#8221</br>Joan of Arc'),
    pg.HabitLeft("", "Goals & Intentions"),
    pg.HabitRight("", "Self Encouragement"),
    pg.CalLeft("", 2, 2024, holiday.holidayMaster),
    pg.CalRight("", 2, 2024, holiday.holidayMaster),
    pg.Week("", [4, 5, 6, 7, 8, 9, 10]),
    pg.Day("", "Monday, September 4"),
    pg.Day("", "Tuesday, sepember 5"),
    pg.Day("", "Wednesday, September 6"),
    pg.Day("", "Thursday, September 7"),
    pg.Day("", "Friday, September 8"),
    pg.Day("", "Saturday, September 9"),
    pg.Day("", "Sunday, September 10"),
    pg.Week("", [11, 12, 13, 14, 15, 16, 17]),
    pg.Day("", "Monday, September 11"),
    pg.Day("", "Tuesday, sepember 12"),
    pg.Day("", "Wednesday, September 13"),
    pg.Day("", "Thursday, September 14"),
    pg.Day("", "Friday, September 15"),
    pg.Day("", "Saturday, September 16"),
    pg.Day("", "Sunday, September 17"),
    pg.Week("", [18, 19, 20, 21, 22, 23, 24]),
    pg.Day("", "Monday, September 18"),
    pg.Day("", "Tuesday, sepember 19"),
    pg.Day("", "Wednesday, September 20"),
    pg.Day("", "Thursday, September 21"),
    pg.Day("", "Friday, September 22"),
    pg.Day("", "Saturday, September 23"),
    pg.Day("", "Sunday, September 24"),
    pg.Week("", [25, 26, 27, 28, 29, 30, 31]),
    pg.Day("", "Monday, September 25"),
    pg.Day("", "Tuesday, sepember 26"),
    pg.Day("", "Wednesday, September 27"),
    pg.Day("", "Thursday, September 28"),
    pg.Day("", "Friday, September 29"),
    pg.Day("", "Saturday, September 30"),
    pg.Day("", "Sunday, october 1"),
    pg.Lined(""),
    pg.Lined(""),
    pg.Lined(""),
    pg.Lined(""),
    pg.Graph(""),
    pg.Graph(""),
    pg.Question("", "What did you learn this month?"),
]

#Create 5x8 & A5slim planners
feb24_planner = pln.Planner('October', '2023', 0, 29, myPlanner=feb24)
feb24_planner.createPlanner(filename='feb24_5x8.html', size='5x8')
feb24_planner.createPlanner(filename='feb24_A5slim.html', size='A5slim')
