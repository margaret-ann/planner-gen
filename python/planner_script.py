#!/usr/bin/env python
# coding: utf-8

#import copy
import calendar as cal
import shutil as st

# Reorder pages from reader spread to printer spread
#def reorder_booklet(pages):
#    """ Input is list ordered by reader page number. Returns list ordered by print page number. """
#    read_order = copy.deepcopy(pages)
#    print_order = []
#    if len(read_order) % 2 == 0:
#        print_order.append(read_order.pop(len(read_order)-1)) #pop back
#        front = True
#        for num in range(int((len(pages)-2)/2)):
#            if front == True:
#                print_order.append(read_order.pop(0)) #pop front
#                print_order.append(read_order.pop(0)) #pop front
#                front = not front
#            elif front == False:
#                print_order.append(read_order.pop(len(read_order)-1)) #pop back
#                print_order.append(read_order.pop(len(read_order)-1)) #pop back
#                front = not front
#        print_order.append(read_order.pop(0)) #pop final page
#        return print_order
#    else:
#        print("booklet must be size divisible by 2")


# 'Planner' class hierarchy
class Planner:
    def __init__(self, month, year, filename, startDate, endDate, startWeekDay="Mon", myPlanner=[]):
        self.myPlanner = myPlanner #data structure to hold Page objects
        self.month = month
        self.year = year
        self.filename = filename
        self.startDate = startDate
        self.endDate = endDate
        self.startWeekDay = startWeekDay

    def addPage(self):
        """ Initialize new Page object & add it to the end of myPlanner """

    def getPrinterSpread(self):
        """ Return Page objects ordered by printer spread """
        print_order = []
        frontPointer = 0
        backPointer = len(self.myPlanner) - 1
        if len(self.myPlanner) % 2 == 0:
            print_order.append(self.myPlanner[backPointer]) #pop back
            backPointer = backPointer - 1 #update pointer
            front = True
            for num in range(int((len(self.myPlanner)-2)/2)):
                if front == True:
                    print_order.append(self.myPlanner[frontPointer]) #pop front
                    frontPointer = frontPointer + 1 #update pointer
                    print_order.append(self.myPlanner[frontPointer]) #pop front
                    frontPointer = frontPointer + 1 #update pointer
                    front = not front
                elif front == False:
                    print_order.append(self.myPlanner[backPointer]) #pop back
                    backPointer = backPointer - 1 #update pointer
                    print_order.append(self.myPlanner[backPointer]) #pop back
                    backPointer = backPointer - 1 #update pointer
                    front = not front
            print_order.append(self.myPlanner[frontPointer]) #pop final page
            return print_order
        else:
            print("booklet must be size divisible by 2")

    def getReaderSpread(self):
        """ Return Page objects ordered by reader spread """
        return self.myPlanner

    def createPlanner(self, size='5x8'):
        """ Run createPage() for all Pages in Planner, writes HTML file to out folder """
        printPlanner = self.getPrinterSpread()

        f = open(f'../out/{self.filename}', "w")
    
        # html head
        fhead = open(f'../page_html/{size}/head.html', "r")
        for line in fhead:
            f.write(line)

        # html body
        f.write("""
        <!-- Content of the booklet -->
        <body>""")
            
        for index in range(int(len(printPlanner)/4)):

            #page1
            f.write("""
            
            <div class="page">
    """)
            f.write(printPlanner[4*index].createPage(size))

            #page2
            f.write(printPlanner[4*index+1].createPage(size))
            f.write("""
                </div>
    """)

            #page3
            f.write("""
            
            <div class="page">
    """)
            f.write(printPlanner[4*index+2].createPage(size))

            #page4
            f.write(printPlanner[4*index+3].createPage(size))
            f.write("""
            </div>
            """)
                
        f.write("""
        
        </body>
                """)
    
        f.close()
       

# 'Page' class hierarchy
class Page:
    def __init__(self, type, section, htmlTemp):
        self.type = type
        self.section = section
        self.htmlTemp = htmlTemp

    def setSection(self, newSection):
        """ Set the section variable """
        self.section = newSection
        return newSection

    def getSection(self):
        """ Return the section variable """
        return self.section

    def getType(self):
        """ Return the type variable """
        return self.type

    def createPage(self, size):
        """ Returns html for the page based on tempate & section """
        html = ""
        f = open(f'../page_html/{size}/{self.htmlTemp}', "r")
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
        f = open(f'../page_html/{size}/{self.htmlTemp}', "r")
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
        f = open(f'../page_html/{size}/{self.htmlTemp}', "r")
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
        f = open(f'../page_html/{size}/{self.htmlTemp}', "r")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{heading}}" in line:
                line = line.replace("{{heading}}", self.heading)
            html += line
        f.close()
        return html

class CalLeft(Page):
    def __init__(self, section, type="calLeft", htmlTemp="calleft.html"):
        super().__init__(type, section, htmlTemp)

    def createPage(self, size):
        """ Returns html for the page based on tempate & instance variables """
        html = ""
        f = open(f'../page_html/{size}/{self.htmlTemp}', "r")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            html += line
        f.close()
        return html

class CalRight(Page):
    def __init__(self, section, type="calRight", htmlTemp="calright.html"):
        super().__init__(type, section, htmlTemp)

    def createPage(self, size):
        """ Returns html for the page based on tempate & instance variables """
        html = ""
        f = open(f'../page_html/{size}/{self.htmlTemp}', "r")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            html += line
        f.close()
        return html

class Week(Page):
    def __init__(self, section, days, type="week", htmlTemp="week.html"):
        super().__init__(type, section, htmlTemp)
        self.days = days

    def getOrdinal(self, num):
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
        f = open(f'../page_html/{size}/{self.htmlTemp}', "r")
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
    def __init__(self, section, date, type="day", htmlTemp="day.html"):
        super().__init__(type, section, htmlTemp)
        self.date = date

    def createPage(self, size):
        """ returns html for the page based on tempate & instance variables """
        html = ""
        f = open(f'../page_html/{size}/{self.htmlTemp}', "r")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{date}}" in line:
                line = line.replace("{{date}}", self.date)
            html += line
        f.close()
        return html

class Lined(Page):
    def __init__(self, section, type="lined", htmlTemp="lined.html"):
        super().__init__(type, section, htmlTemp)

    def createPage(self, size):
        """ returns html for the page based on tempate & instance variables """
        html = ""
        f = open(f'../page_html/{size}/{self.htmlTemp}', "r")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            html += line
        f.close()
        return html

class Graph(Page):
    def __init__(self, section, type="graph", htmlTemp="graph.html"):
        super().__init__(type, section, htmlTemp)

    def createPage(self, size):
        """ returns html for the page based on tempate & instance variables """
        html = ""
        f = open(f'../page_html/{size}/{self.htmlTemp}', "r")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
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
        f = open(f'../page_html/{size}/{self.htmlTemp}', "r")
        for line in f:
            if "{{section}}" in line:
                line = line.replace("{{section}}", self.section)
            if "{{question}}" in line:
                line = line.replace("{{question}}", self.question)
            html += line
        f.close()
        return html


# writing the html
page_list = [Cover("", 'October', '2023', '&#8220Adopt the pace of nature: her secret is patience.&#8221</br>Ralph Waldo Emerson'),
            HabitLeft("", "Goals & Intentions"),
            HabitRight("", "Self Encouragement"),
            CalLeft(""),
            CalRight(""),
            Week("", [4, 5, 6, 7, 8, 9, 10]),
            Day("", "Monday, September 4"),
            Day("", "Tuesday, sepember 5"),
            Day("", "Wednesday, September 6"),
            Day("", "Thursday, September 7"),
            Day("", "Friday, September 8"),
            Day("", "Saturday, September 9"),
            Day("", "Sunday, September 10"),
            Week("", [11, 12, 13, 14, 15, 16, 17]),
            Day("", "Monday, September 11"),
            Day("", "Tuesday, sepember 12"),
            Day("", "Wednesday, September 13"),
            Day("", "Thursday, September 14"),
            Day("", "Friday, September 15"),
            Day("", "Saturday, September 16"),
            Day("", "Sunday, September 17"),
            Week("", [18, 19, 20, 21, 22, 23, 24]),
            Day("", "Monday, September 18"),
            Day("", "Tuesday, sepember 19"),
            Day("", "Wednesday, September 20"),
            Day("", "Thursday, September 21"),
            Day("", "Friday, September 22"),
            Day("", "Saturday, September 23"),
            Day("", "Sunday, September 24"),
            Week("", [25, 26, 27, 28, 29, 30, 31]),
            Day("", "Monday, September 25"),
            Day("", "Tuesday, sepember 26"),
            Day("", "Wednesday, September 27"),
            Day("", "Thursday, September 28"),
            Day("", "Friday, September 29"),
            Day("", "Saturday, September 30"),
            Day("", "Sunday, october 1"),
            Lined(""),
            Lined(""),
            Lined(""),
            Lined(""),
            Graph(""),
            Graph(""),
            Question("", "What did you learn this month?"),
                   ]

def setSections(pageList):
    """ Assign printed page orientation to each page based on list order """
    if len(pageList) % 2 == 0:
        for index in range(int(len(pageList)/4)):
            pageList[4*index].setSection("left_front")
            pageList[4*index+1].setSection("right_front")
            pageList[4*index+2].setSection("left_back")
            pageList[4*index+3].setSection("right_back")
    else:
        print("Booklet must be size divisible by 2")

#def build_book(month, year, pageList, fileout):
#    """ Assemble html of the book """
#    f = open(f"../out/{fileout}", "w")
#    
#    # html head
#    fhead = open('../page_html/head.html', "r")
#    for line in fhead:
#        f.write(line)
#
#    # html body
#    f.write("""
#    <!-- content of the booklet -->
#    <body>""")
#            
#    for index in range(int(len(pageList)/4)):
#
#        #page1
#        f.write("""
#        
#        <div class="page">
#""")
#        f.write(pageList[4*index].createPage())
#
#        #page2
#        f.write(pageList[4*index+1].createPage())
#        f.write("""
#            </div>
#""")
#
#        #page3
#        f.write("""
#        
#        <div class="page">
#""")
#        f.write(pageList[4*index+2].createPage())
#
#        #page4
#        f.write(pageList[4*index+3].createPage())
#        f.write("""
#        </div>
#        """)
#                
#    f.write("""
#    
#    </body>
#            """)
#    
#    f.close()



#Set up list of pages 
setSections(page_list)

#Create 5x8 planner
planner_5x8 = Planner('October', '2023', 'oct23_5x8.html', 0, 31, myPlanner=page_list)
planner_5x8.createPlanner(size='5x8')

#Create A5 Slim planner
planner_A5slim = Planner('October', '2023', 'oct23_A5slim.html', 0, 31, myPlanner=page_list)
planner_A5slim.createPlanner(size='A5slim')
