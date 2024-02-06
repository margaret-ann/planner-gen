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

    def addWeekofDays(self, myDay, myPrompts):
        """ Add full week of daily pages """
        myDays = []
        iso_date = myDay.isocalendar()
        cal_day = myDay.fromisocalendar(iso_date[0], iso_date[1], 1)
        delta = datetime.timedelta(days=1)
        for i in range(7):
            self.addPage(pg.Day("", cal_day, myPrompts))
            cal_day += delta

    def setSections(self):
        """ Assign printed page orientation to each page based on list order """
        if len(self.myPlanner) % 2 == 0:
            for index in range(int(len(self.myPlanner)/4)):
                self.myPlanner[4*index].setSection("left_front")
                self.myPlanner[4*index+1].setSection("right_front")
                self.myPlanner[4*index+2].setSection("left_back")
                self.myPlanner[4*index+3].setSection("right_back")
        else:
            print("Booklet must be size divisible by 2")

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

    def createPlanner(self, filename='out.html', size='5x8', spread='printer'):
        """ Run createPage() for all Pages in Planner, writes HTML file to out folder """
        self.size = size
        self.spread = spread
        
        if spread == 'printer':
            self.setSections()
            newPlanner = self.getPrinterSpread()
        elif spread == 'reader':
            self.setSections() #replace this soon
            newPlanner = self.getReaderSpread()

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