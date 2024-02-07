import datetime
import page as pg

# 'Planner' class hierarchy
class Planner:
    def __init__(self, startDate, endDate, startWeekDay="Mon", myPlanner=[]):
        self.myPlanner = myPlanner #data structure to hold Page objects
        self.startDate = startDate
        self.endDate = endDate
        self.startWeekDay = startWeekDay

    def addPage(self, newPage):
        """ Add page object to end of planner list """
        self.myPlanner.append(newPage)

    def printPlannerSummary(self):
        """ Add page object to end of planner list """
        for i in range(len(self.myPlanner)):
            print(f"Page {i}: {self.myPlanner[i].getType()}")

    def addWeekofDays(self, myDay, myPrompts):
        """ Add full week of daily pages """
        myDays = []
        iso_date = myDay.isocalendar()
        cal_day = myDay.fromisocalendar(iso_date[0], iso_date[1], 1)
        delta = datetime.timedelta(days=1)
        for i in range(7):
            self.addPage(pg.Day("", cal_day, myPrompts))
            cal_day += delta

    def setSections(self, myBook):
        """ Assign printed page orientation to each page based on list order """
        if len(myBook) % 2 == 0:
            for index in range(int(len(myBook)/4)):
                myBook[4*index].setSection("left_front")
                myBook[4*index+1].setSection("right_front")
                myBook[4*index+2].setSection("left_back")
                myBook[4*index+3].setSection("right_back")
            return myBook
        else:
            print("Booklet must be size divisible by 2")

    def getPrinterSpread(self, perPage=2):
        """ Return Page objects ordered by printer spread """
        print_order = []
        frontPointer = 0
        backPointer = len(self.myPlanner) - 1
        if len(self.myPlanner) % 2 != 0:
            print("booklet must be size divisible by 2")

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

        if perPage == 2:
            return print_order
        elif perPage == 4:
            print_tup = []
            for i, elem in enumerate(print_order):
                if i%2 == 1:
                    print_tup.append((print_order[i-1], print_order[i]))
            for i, elem in enumerate(print_tup):
                if i%4 == 3:
                    temp = print_tup[i-2]
                    print_tup[i-2] = print_tup[i-1]
                    print_tup[i-1] = temp
            print_order_4 = []
            for one, two in print_tup:
                print_order_4.append(one)
                print_order_4.append(two)
            return print_order_4
        else:
            print(f"Printing {perPage} planner pages per printer page is not supported")

    def getReaderSpread(self):
        """ Return Page objects ordered by reader spread """
        return self.myPlanner

    def createPlanner(self, filename='out.html', size='5x8', spread='printer'):
        """ Run createPage() for all Pages in Planner, writes HTML file to out folder """
        self.size = size
        self.spread = spread
        
        if self.spread == 'printer':
            if (self.size == '5x8') or (self.size == 'A5slim'):
                newPlanner = self.getPrinterSpread(perPage=2)
            elif self.size == '3x5':
                newPlanner = self.getPrinterSpread(perPage=4)
            newPlanner = self.setSections(newPlanner)
        elif self.spread == 'reader':
            newPlanner = self.getReaderSpread()
            newPlanner = self.setSections(newPlanner) #replace this soon

        f = open(f'./out/{filename}', 'w', encoding='utf-8')
    
        # html head
        fhead = open(f'./page_html/head.html', 'r', encoding='utf-8')
        for line in fhead:
            if "{{size}}" in line:
                line = line.replace("{{size}}", size)
            f.write(line)

        # html body
        f.write("""
        <!-- Content of the booklet -->
        <body>""")
            
        for index in range(int(len(newPlanner)/4)):

            #page1
            f.write("""
            
            <div class="page">
    """)
            f.write(newPlanner[4*index].createPage(size))

            #page2
            f.write(newPlanner[4*index+1].createPage(size))
            f.write("""
                </div>
    """)

            #page3
            f.write("""
            
            <div class="page">
    """)
            f.write(newPlanner[4*index+2].createPage(size))

            #page4
            f.write(newPlanner[4*index+3].createPage(size))
            f.write("""
            </div>
            """)
                
        f.write("""
        
        </body>
                """)
    
        f.close()