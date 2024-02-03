#2024 holiday information
#TODO: Make programmable for all years
holiday_list = []

#USA Federal Holidays
holidayFederal = [
    [(1,"New Year's Day"), (15,"MLK Day")], #Jan
    [(19, "Washington's Birthday")], #Feb
    [], #Mar
    [], #Apr
    [(27, "Memorial Day")], #May
    [(19, "Juneteenth")], #Jun
    [(4, "Independence Day")], #Jul
    [], #Aug
    [(2, "Labor Day")], #Sep
    [(14, "Indigenous People's Day")], #Oct
    [(11, "Veterans Day"), (28, "Thanksgiving")], #Nov
    [(25, "Christmas")], #Dec
]
holiday_list.append(holidayFederal)

#USA Common Holidays
holidayCommon = [
    [], #Jan
    [(2, "Groundhog Day"), (10, "Mardi Gras"), (14, "Valentine's Day"), (29, "Leap Day")], #Feb
    [(10, "Daylight Saving Time"), (17, "St. Patrick's Day"), (31, "Easter")], #Mar
    [(8, "Total Solar Eclipse"), (15, "Tax Day")], #Apr
    [(5, "Cinco de Mayo"), (12, "Mother's Day")], #May
    [(16, "Father's Day")], #Jun
    [], #Jul
    [], #Aug
    [], #Sep
    [(31, "Halloween")], #Oct
    [(3, "Day Saving Time")], #Nov
    [(24, "Christmas Eve"), (31, "New Year's Eve")], #Dec
]
holiday_list.append(holidayCommon)

#Pagan Wheel of the Year
holidayPagan = [
    [], #Jan
    [(2, "Imbolc")], #Feb
    [(21, "Ostara")], #Mar
    [], #Apr
    [(1, "Beltane")], #May
    [(21, "Litha")], #Jun
    [], #Jul
    [(1, "Lughnasadh")], #Aug
    [(21, "Mabon")], #Sep
    [(31, "Samhain")], #Oct
    [], #Nov
    [(21, "Yule")], #Dec
]
holiday_list.append(holidayPagan)

#Fun Holidays
holidayFun = [
    [(4, "Trivia Day"), (5, "Bird Day"), (21, "Squirrel Appreciation Day"), (27, "Chocolate Cake Day")], #Jan
    [(17, "Random Act of Kindness Day")], #Feb
    [(14, "Pi Day")], #Mar
    [], #Apr
    [(4, "Star Wars Day")], #May
    [(13, "Sewing Machine Day")], #Jun
    [(21, "Ice Cream Day")], #Jul
    [(2, "International Beer Day")], #Aug
    [(19, "Talk Like a Pirate Day"), (21, "Batman Day"), (22, "Hobit Day")], #Sep
    [(1, "International Coffee Day"), (29, "Internet Day")], #Oct
    [(13, "World Kindness Day"), (22, "Buy Nothing Day")], #Nov
    [(9, "Christmas Card Day"), (21, "Ugly Sweater Day")], #Dec
]
holiday_list.append(holidayFun)

#Political Events
holidayPolitical = [
    [(15, "Iowa Caucus"), (23, "NH Primary")], #Jan
    [(3, "South Carolina Primary")], #Feb
    [(5, "Super Tuesday"), (7, "State of the Union")], #Mar
    [], #Apr
    [], #May
    [], #Jun
    [(18, "Republican National Convention")], #Jul
    [(19, "Democratic National Covention")], #Aug
    [], #Sep
    [], #Oct
    [(5, "Election Day")], #Nov
    [], #Dec
]
holiday_list.append(holidayPolitical)

# Master holiday list
holidayMaster = [{},{},{},{},{},{},{},{},{},{},{},{}]
for group in holiday_list:
    for index, month in enumerate(group):
        for holiday in month:
            if holiday[0] in holidayMaster[index]: #key already exists
                holidayMaster[index][holiday[0]].append(holiday[1])
            else: #new key
                holidayMaster[index][holiday[0]] = [holiday[1]]

# template to add new holiday set
holidayTemplate = [
    [], #Jan
    [], #Feb
    [], #Mar
    [], #Apr
    [], #May
    [], #Jun
    [], #Jul
    [], #Aug
    [], #Sep
    [], #Oct
    [], #Nov
    [], #Dec
]