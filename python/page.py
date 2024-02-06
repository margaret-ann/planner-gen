import calendar as cal
import datetime

# 'Page' class hierarchy
class Page:

    def __init__(self, type, section, htmlTemp):
        self.type = type
        self.section = section
        self.htmlTemp = htmlTemp

        self.weekDict = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday",
        }

        self.monthDict = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        }

    def setSection(self, newSection):
        """ Set the section variable """
        self.section = newSection

    def getSection(self):
        """ Return the section variable """
        return self.section

    def getType(self):
        """ Return the type variable """
        return self.type

    def createPage(self, size):
        """ Returns html for the page based on tempate & section """
        html = ""
        f = open(f'./page_html/{self.htmlTemp}', "r", encoding="utf-8")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            html += line
        f.close()
        return html

class Cover(Page):
    def __init__(self, section, title, subtitle, tag, type="cover", htmlTemp="cover.html"):
        super().__init__(type, section, htmlTemp)
        self.title = title
        self.subtitle = subtitle
        self.tag = tag

    def createPage(self, size):
        """ Returns html for the page based on tempate & instance variables """
        html = ""
        f = open(f'./page_html/{self.htmlTemp}', "r", encoding="utf-8")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{title}}" in line:
                line = line.replace("{{title}}", self.title)
            if "{{subtitle}}" in line:
                line = line.replace("{{subtitle}}", self.subtitle)
            if "{{tag}}" in line:
                line = line.replace("{{tag}}", self.tag)
            html += line
        f.close()
        return html

class HabitLeft(Page):
    def __init__(self, section, heading, type="habitLeft", htmlTemp="habitleft.html"):
        super().__init__(type, section, htmlTemp)
        self.heading = heading

    def createPage(self, size):
        """ Returns html for the page based on tempate & instance variables """
        html = ""
        f = open(f'./page_html/{self.htmlTemp}', "r", encoding="utf-8")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{heading}}" in line:
                line = line.replace("{{heading}}", self.heading)
            html += line
        f.close()
        return html

class HabitRight(Page):
    def __init__(self, section, heading, type="habitRight", htmlTemp="habitright.html"):
        super().__init__(type, section, htmlTemp)
        self.heading = heading

    def createPage(self, size):
        """ Returns html for the page based on tempate & instance variables """
        html = ""
        f = open(f'./page_html/{self.htmlTemp}', "r", encoding="utf-8")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{heading}}" in line:
                line = line.replace("{{heading}}", self.heading)
            html += line
        f.close()
        return html

class CalLeft(Page):
    def __init__(self, section, month, year, holiday, type="calLeft", htmlTemp="calleft.html"):
        super().__init__(type, section, htmlTemp)
        self.month = month
        self.year = year
        self.holiday = holiday

        #Create days list
        obj = cal.Calendar()
        self.days = []
        for index, day in enumerate(obj.itermonthdays(self.year, self.month)):
            if (index+1)%7 == 1 or (index+1)%7 == 2 or (index+1)%7 == 3 or (index+1)%7 == 4:
                if day == 0:
                    self.days.append("*")
                else:
                    self.days.append(day)

        #Pull holiday dictionary for correct month
        self.myHoliday = self.holiday[month-1]

    def createPage(self, size):
        """ Returns html for the page based on tempate & instance variables """
        html = ""
        day_index = 0
        f = open(f'./page_html/{self.htmlTemp}', "r", encoding="utf-8")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{date}}" in line:
                line = line.replace("{{date}}", str(self.days[day_index]))
                day_index += 1
            if "{{holiday}}" in line:
                if self.days[day_index-1] in self.myHoliday:
                    line = line.replace("{{holiday}}", self.myHoliday[self.days[day_index-1]][0])
                else:
                    line = line.replace("{{holiday}}", "</br></br></br></br>")
            html += line
        f.close()

        #TODO: add moon phase to calendar
        #<p id="holiday">Full Moon <span id="full_moon">&#9677</span></p>
        #<p id="holiday">New Moon <span id="new_moon">&#9711</span></p> <!-- 9711 -->
        #<p id="holiday">Half Moon <span id="half_moon">&#9680</span></p> <!-- 9680 -->

        return html

class CalRight(Page):
    def __init__(self, section, month, year, holiday, type="calRight", htmlTemp="calright.html"):
        super().__init__(type, section, htmlTemp)
        self.month = month
        self.year = year
        self.holiday = holiday

        #Create days list
        obj = cal.Calendar()
        self.days = []
        for index, day in enumerate(obj.itermonthdays(self.year, self.month)):
            if (index+1)%7 == 5 or (index+1)%7 == 6 or (index+1)%7 == 0:
                if day == 0:
                    self.days.append("*")
                else:
                    self.days.append(day)

        #Pull holiday dictionary for correct month
        self.myHoliday = self.holiday[month-1]

    def createPage(self, size):
        """ Returns html for the page based on tempate & instance variables """
        html = ""
        day_index = 0
        f = open(f'./page_html/{self.htmlTemp}', "r", encoding="utf-8")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{date}}" in line:
                line = line.replace("{{date}}", str(self.days[day_index]))
                day_index += 1
            if "{{holiday}}" in line:
                if self.days[day_index-1] in self.myHoliday:
                    line = line.replace("{{holiday}}", self.myHoliday[self.days[day_index-1]][0])
                else:
                    line = line.replace("{{holiday}}", "</br></br></br></br>")
            html += line
        f.close()
        return html

class Week(Page):
    def __init__(self, section, date, type="week", htmlTemp="week.html"):
        super().__init__(type, section, htmlTemp)
        self.date = date #can be any date within the week

        #generate days list from date
        self.days = []
        iso_date = self.date.isocalendar()
        cal_day = date.fromisocalendar(iso_date[0], iso_date[1], 1)
        delta = datetime.timedelta(days=1)
        for i in range(7):
            self.days.append(cal_day.day)
            cal_day += delta

    def getOrdinal(self, num):
        """ Returns ordinal string for date """
        if num in [1, 21, 31]:
            return "st"
        elif num in [2, 22]:
            return "nd"
        elif num in [3, 23]:
            return "rd"
        elif num in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 26, 27, 28, 29, 30]:
            return "th"
    
    def createPage(self, size):
        """ returns html for the page based on tempate & instance variables """
        html = ""
        f = open(f'./page_html/{self.htmlTemp}', "r", encoding="utf-8")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{day1}}" in line:
                line = line.replace("{{day1}}", str(self.days[0]))
            if "{{day2}}" in line:
                line = line.replace("{{day2}}", str(self.days[1]))
            if "{{day3}}" in line:
                line = line.replace("{{day3}}", str(self.days[2]))
            if "{{day4}}" in line:
                line = line.replace("{{day4}}", str(self.days[3]))
            if "{{day5}}" in line:
                line = line.replace("{{day5}}", str(self.days[4]))
            if "{{day6}}" in line:
                line = line.replace("{{day6}}", str(self.days[5]))
            if "{{day7}}" in line:
                line = line.replace("{{day7}}", str(self.days[6]))
            if "{{sup1}}" in line:
                line = line.replace("{{sup1}}", self.getOrdinal(self.days[0]))
            if "{{sup2}}" in line:
                line = line.replace("{{sup2}}", self.getOrdinal(self.days[1]))
            if "{{sup3}}" in line:
                line = line.replace("{{sup3}}", self.getOrdinal(self.days[2]))
            if "{{sup4}}" in line:
                line = line.replace("{{sup4}}", self.getOrdinal(self.days[3]))
            if "{{sup5}}" in line:
                line = line.replace("{{sup5}}", self.getOrdinal(self.days[4]))
            if "{{sup6}}" in line:
                line = line.replace("{{sup6}}", self.getOrdinal(self.days[5]))
            if "{{sup7}}" in line:
                line = line.replace("{{sup7}}", self.getOrdinal(self.days[6]))
            html += line
        f.close()
        return html

class Day(Page):
    def __init__(self, section, date, prompts=[None,None,None], type="day", htmlTemp="day.html"):
        super().__init__(type, section, htmlTemp)
        self.date = date
        self.prompts = prompts

    def createPage(self, size):
        """ returns html for the page based on tempate & instance variables """
        html = ""
        prompt_cnt = 0
        f = open(f'./page_html/{self.htmlTemp}', "r", encoding="utf-8")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{date}}" in line:
                line = line.replace("{{date}}", f"{self.weekDict[self.date.weekday()]}, {self.monthDict[self.date.month]} {self.date.day}")
            if "{{prompt}}" in line:
                line = line.replace("{{prompt}}", self.prompts[prompt_cnt])
                prompt_cnt += 1
            html += line
        f.close()
        return html

class Lined(Page):
    def __init__(self, section, type="lined", htmlTemp="lined.html"):
        super().__init__(type, section, htmlTemp)

    def createPage(self, size):
        """ returns html for the page based on tempate & instance variables """
        html = ""
        line_html = ""
        line_cnt = 0

        if size == '5x8':
            line_cnt = 29
        elif size == 'A5slim':
            line_cnt = 30
        elif size == '3x5':
            line_cnt = 26

        for l in range(line_cnt):
            line_html += '<p class="line"><hr class="line"></hr></p>'

        f = open(f'./page_html/{self.htmlTemp}', "r", encoding="utf-8")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{lines}}" in line:
                line = line.replace("{{lines}}", line_html)
            html += line
        f.close()
        return html

class Graph(Page):
    def __init__(self, section, type="graph", htmlTemp="graph.html"):
        super().__init__(type, section, htmlTemp)

    def createPage(self, size):
        """ returns html for the page based on tempate & instance variables """
        html = ""
        row = 0
        col = 0

        # choose grid based on size
        if size == '5x8' or size == 'A5slim':
            row = 16
            col = 26
        elif size == '3x5':
            row = 11
            col = 19

        grid_html = ""
        for c in range(col):
            grid_html += "<tr>\n"
            for r in range(row):
                grid_html += "<th></th>\n"
            grid_html += "</tr>\n"

        f = open(f'./page_html/{self.htmlTemp}', "r", encoding="utf-8")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{grid}}" in line:
                line = line.replace("{{grid}}", grid_html)
            html += line
        f.close()
        return html

class Question(Page):
    def __init__(self, section, question, type="question", htmlTemp="question.html"):
        super().__init__(type, section, htmlTemp)
        self.question = question

    def createPage(self, size):
        """ returns html for the page based on tempate & instance variables """
        html = ""
        line_html = ""
        lines = 0

        if size == '5x8':
            lines = 28
        elif size == 'A5slim':
            lines = 30
        elif size == '3x5':
            lines = 25

        for line in range(lines):
            line_html += '<p class="line"><hr class="line"></hr></p>\n'

        f = open(f'./page_html/{self.htmlTemp}', "r", encoding="utf-8")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{question}}" in line:
                line = line.replace("{{question}}", self.question)
            if "{{lines}}" in line:
                line = line.replace("{{lines}}", line_html)
            html += line
        f.close()
        return html